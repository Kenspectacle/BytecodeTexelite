import subprocess
import os

functionsToSkip = []

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
    global functionsToSkip
    functionsToSkip = []  # Reset functionsToSkip for each file

    counter = 0
    subfolder = FileName = None
    StartLine = EndLine = None
    function_size_limit = 15

    for line in lines:
        subfolder = parse_line(line, "SubFolder=\"") or subfolder
        FileName = parse_line(line, "FileName=\"") or FileName
        StartLine = parse_line_int(line, "StartLine=") or StartLine

        if "EndLine=" in line:
            line = line.strip()
            EndLine = parse_line_int(line, "EndLine=")
            function_size = EndLine - StartLine + 1
            if function_size < function_size_limit:
                functionsToSkip.append(counter)
                print(f"Function {counter} : {subfolder},{FileName},{StartLine},{EndLine} has less than {function_size_limit} lines.")
            else:
                result = f"{subfolder},{FileName},{StartLine},{EndLine}"
                print(f"Function {counter} : {result}")
                result_lines.append(result)
            counter += 1

def process_javap_c_output(lines):
    """Process the javap -c output to match functions."""
    line_count = 0
    skip = False
    function_count = 0
    non_skipped_function_count = -1
    startline_of_bc = 0
    endline_of_bc = 0
    bc_filename = ""

    # initialize skip
    if 0 in functionsToSkip:
        skip = True

    for line in lines:
        line = line.strip()  # Strip extra whitespace
        line_count += 1


        # Get filename for the bc file
        if line_count == 2:
            bc_filename = extract_bc_filename(line) or "no bc filename found"
            print(bc_filename)

        # check if the function should be skipped
        if skip:
            if line == "":
                function_count += 1
                if function_count in functionsToSkip:
                    continue
                else:
                    skip = False
            else:
                continue

        else:
            if "Code:" in line:
                startline_of_bc = line_count
                continue
            elif line != "":
                continue
            else:
                function_count += 1
                non_skipped_function_count += 1
                endline_of_bc = line_count - 1

                print(result_lines)

                result_lines[non_skipped_function_count] += f",{startline_of_bc},{endline_of_bc},{bc_filename}"
                print("bc part: ", f",{startline_of_bc},{endline_of_bc},{bc_filename}")
                print("Result_lines: " , result_lines)
                print("RESULT:", result_lines[non_skipped_function_count])
                with open("output_file.csv", "a") as f:
                    f.write(result_lines[non_skipped_function_count] + "\n")

            # Turn on skip for the next function
            if function_count in functionsToSkip:
                skip = True
                continue
            

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
                print(f"Processing {class_file}")
                javap_v_output = generate_javap_output(class_file, '-v')
                javap_c_output = generate_javap_output(class_file, '-c')
                
                process_javap_v_output(javap_v_output)
                process_javap_c_output(javap_c_output)

if __name__ == "__main__":
    class_folder = "sample_for_test"  # Replace with your actual class folder path
    skip_folder_name = "StubClass"  # Replace with the folder name you want to skip
    main(class_folder, skip_folder_name)
