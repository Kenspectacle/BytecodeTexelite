functionsToSkip = []
result_lines = []

def parse_line(line, keyword, delimiter="\""):
    """Helper function to parse lines based on a keyword and delimiter."""
    if keyword in line:
        splittedLine = line.split(delimiter)
        return splittedLine[1]
    return None

def parse_line_int(line, keyword):
    """Helper function to parse lines based on a keyword and convert the result to an integer."""
    if keyword in line:
        line = line.strip()
        splittedLine = line.split(keyword)
        return int(splittedLine[1])
    return None


with open("example1") as file:
    counter = 0
    subfolder = FileName = None
    StartLine = EndLine = None
    function_size_limit = 15
    result_lines = []

    for line in file:
        subfolder = parse_line(line, "SubFolder=\"") or subfolder
        FileName = parse_line(line, "FileName=\"") or FileName
        StartLine = parse_line_int(line, "StartLine=") or StartLine

        

        # Find EndLine
        if ("EndLine=" in line):
            line=line.strip()
            splittedLine = line.split("EndLine=")
            EndLine = int(splittedLine[1])


            # Check if the function is too small, add to the skip list
            function_size = EndLine-StartLine+1
            if function_size < function_size_limit:
                functionsToSkip.append(counter)
                print(f"Function {counter} : {subfolder},{FileName},{StartLine},{EndLine} has less than 15 lines.")
            # Add the results into result_lines
            else:
                result = f"{subfolder},{FileName},{StartLine},{EndLine}"
                print(f"Function {counter} : {result}")
                result_lines.append(result)
                
                
            counter+=1

with open("example2") as file: 
    # initializer
    lineCount = 0
    skip = False
    function_count = 0
    startline_of_bc = 0
    endline_of_bc = 0
    non_skipped_function_count = -1 # 0 index

    for line in file:
        lineCount+=1
        
        
        # skip the first part of a bc file 
        '''
        Compiled from "111424.java"
        abstract class _111424.AbstractTest extends _111424.StubClass.StubClass {
        public _111424.AbstractTest(java.lang.Object);
        '''
        if lineCount==3 and 0 in functionsToSkip:
            skip=True

        # skip this function
        if skip and line !="\n":
            continue

        # new function after skip
        if skip and line =="\n":
            skip=False
            startline_of_bc = lineCount # the startline can be obtained here
            function_count+=1
            continue
        
        # new function after non-skipped function
        elif line=="\n":
            function_count += 1
            non_skipped_function_count += 1
            endline_of_bc = lineCount # the endline of bc

            result_lines[non_skipped_function_count] += f"{startline_of_bc},{endline_of_bc},{FileName},{subfolder}"
            output_file = f"output_file.csv"
            with open(output_file, "a") as f:
                f.write(result_lines[non_skipped_function_count] + "\n")

        # turns on skip for the next function
        if (function_count in functionsToSkip):
            skip=True
            continue

        # print(line.strip())

        # Write CSV for finding the substitute startline and endline

        # Produce 1 CSV file in the script
        ## 1. Information of the Javafile
        ## 2. Information of the bc file
        ### use it to compare it with the result from NiCad and exchange the information based on the created CSV (need another script)

        # example entry:
        # subfolder, javafilename, startline, endline, startline bc, endline bc, bc filename, subfolder bc
        # try to figure out how to get the startline and endline of the bc file