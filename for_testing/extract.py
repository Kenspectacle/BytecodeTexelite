import subprocess
import os

functions_to_skip = []

def parse_line(line, keyword, delimiter="\""):
    """Helper function to parse lines based on a keyword and delimiter."""
    if keyword in line:
        splitted_line = line.split(delimiter)
        return splitted_line[1]
    return None

def parse_line_int(line, keyword):
    """Helper function to parse lines based on a keyword and convert the result to an integer."""
    if keyword in line:
        line = line.strip()
        splitted_line = line.split(keyword)
        return int(splitted_line[1])
    return None

def extract_bc_filename(line):
    """Extract the filename from a line containing 'Compiled from'."""
    dot_index = line.find('.')
    if dot_index != -1:
        substring = line[dot_index + 1:]
        end_index = len(substring)
        for i, char in enumerate(substring):
            if char.isspace():
                end_index = i
                break
        return substring[:end_index]
    return None

def generate_javap_output(class_file, option):
    """Generate the javap output for a given .class file with a specified option."""
    result = subprocess.run(['javap', option, class_file], capture_output=True, text=True)
    return result.stdout.splitlines()

def process_javap_v_output(lines):
    """Process the javap -v output to determine functions to skip and collect subfolder information."""
    global functions_to_skip
    functions_to_skip = []  # Reset functions_to_skip for each file

    counter = 0
    subfolder = FileName = None
    StartLine = EndLine = None
    function_size_limit = 15
    has_annotated_constructor = False
    is_in_constructor = True
    Code_counter = 0
    has_endline = False
    first_function = True


    for line in lines:
        if counter == 1:
            first_function = False

        if "Code:" in line:
            if not has_endline and not first_function:
                functions_to_skip.append(counter)
                print(f"Function {counter} : does not have annotation")
                # goes to the next function
                counter += 1
            # reinitialize has_endline
            has_endline = False
            Code_counter += 1
            # print(Code_counter)

        if Code_counter > 1:
            is_in_constructor = False

        # if it doesn't have an annotated constructor
        if (not has_annotated_constructor and not is_in_constructor and counter == 0):
            functions_to_skip.append(counter)
            print(f"Function {counter} : is a default generated constructor and will be skipped")
            counter += 1

        # special conditions for the constructor
        if counter == 0:
            # Proceed as normal
            subfolder = parse_line(line, "SubFolder=\"") or subfolder
            FileName = parse_line(line, "FileName=\"") or FileName
            StartLine = parse_line_int(line, "StartLine=") or StartLine

            # if it is annotated it proceeds as normal
            if "EndLine=" in line:
                has_endline = True

            
                line = line.strip()
                EndLine = parse_line_int(line, "EndLine=")
                function_size = EndLine - StartLine + 1
                if function_size < function_size_limit:
                    functions_to_skip.append(counter)
                    print(f"Function {counter} : constructor {subfolder},{FileName},{StartLine},{EndLine} has less than {function_size_limit} lines.")
                else:
                    result = f"{subfolder},{FileName},{StartLine},{EndLine}"
                    print(f"Function {counter} : contructor{result}")
                    result_lines.append(result)
                counter += 1
                has_annotated_constructor = True
                continue
            else:
                continue
        

        subfolder = parse_line(line, "SubFolder=\"") or subfolder
        FileName = parse_line(line, "FileName=\"") or FileName
        StartLine = parse_line_int(line, "StartLine=") or StartLine

        if "EndLine=" in line:
            has_endline = True
            line = line.strip()
            EndLine = parse_line_int(line, "EndLine=")
            function_size = EndLine - StartLine + 1
            if function_size < function_size_limit:
                functions_to_skip.append(counter)
                print(f"Function {counter} : {subfolder},{FileName},{StartLine},{EndLine} has less than {function_size_limit} lines.")
            else:
                result = f"{subfolder},{FileName},{StartLine},{EndLine}"
                print(f"Function {counter} : {result}")
                result_lines.append(result)
            counter += 1

    # special: for the last function
    if not has_endline:
        functions_to_skip.append(counter)
        print(f"Function {counter} : does not have annotation")

def process_javap_c_output(lines):
    """Process the javap -c output to match functions."""
    line_count = 0
    skip = True
    function_count = -1
    non_skipped_function_count = -1
    startline_of_bc = 0
    endline_of_bc = 0
    bc_filename = ""
    is_in_function = False

    print("functions to skip: ", functions_to_skip)

    for line in lines:
        line1 = line.strip()  # Strip extra whitespace
        line_count += 1

        # DEBUG
        # if function_count == 1:
        #     print(line)
        # print(line)

        # Turn on skip for the next function
        if function_count in functions_to_skip:
            skip = True

        # Get filename for the bc file
        if line_count == 2:
            bc_filename = extract_bc_filename(line1) or "no bc filename found"
            print("bc filename: ", bc_filename)

        # check if the function should be skipped
        if skip:
            if line1 == "Code:":
                startline_of_bc = line_count
                function_count += 1
                print(f"[From Skip] Code: is detected, current function is {function_count}")
                if function_count in functions_to_skip:
                    skip = True
                    continue
                else:
                    is_in_function = True
                    skip = False
            else:
                continue

        else:

            if "Code:" in line1:
                is_in_function = True
                function_count += 1
                print(f"Code: is detected, current function is {function_count}")
                startline_of_bc = line_count
                continue
            elif line1 != "" and line != "}":
                continue
            # skip static initializers
            elif "static {};" in line1:
                skip = True
                continue
            elif "abstract" in line1:
                skip = True
                continue
            elif is_in_function:
                is_in_function = False
                print(f"Function {function_count}: is being processed")
                print("line_count: ", line_count)
                non_skipped_function_count += 1
                print(f"Non skipped function: {non_skipped_function_count}")
                endline_of_bc = line_count - 1

                result_lines[non_skipped_function_count] += f",{startline_of_bc},{endline_of_bc},{bc_filename}"
                print("bc part: ", f",{startline_of_bc},{endline_of_bc},{bc_filename}")
                print("RESULT:", result_lines[non_skipped_function_count])
                
                # print result lines
                print("Result lines:")
                for i, result_line in enumerate(result_lines):
                    if i == non_skipped_function_count: print("> " + result_line)
                    else: print(result_line)
                
                

                # write output into csv
                print(f'writing in: {result_lines[non_skipped_function_count]}')
                with open("output_file.csv", "a") as f:
                    f.write(result_lines[non_skipped_function_count] + "\n")

            
            

def main(class_folder, skip_folder_name):
    print("starting extractor")
    for root, dirs, files in os.walk(class_folder):
        # Skip directories with the specified name
        dirs[:] = [d for d in dirs if d != skip_folder_name]
        print(dirs)
        for file in files:
            if file.endswith(".class"):
                global result_lines
                result_lines = []  # Reset result_lines for each file processed

                class_file = os.path.join(root, file)
                print(f"-------------------separator------------------------")
                print(f"Processing {class_file}")
                javap_v_output = generate_javap_output(class_file, '-v')
                javap_c_output = generate_javap_output(class_file, '-c')
                
                process_javap_v_output(javap_v_output)
                process_javap_c_output(javap_c_output)

if __name__ == "__main__":
    class_folder = "BigCloneBench_Unpacked"  # Replace with your actual class folder path
    skip_folder_name = "StubClass"  # Replace with the folder name you want to skip
    main(class_folder, skip_folder_name)
