import sys

"""
This is a file used for mapping NiCad's output in BigCloneEval format, to the original filename, startline, endline of the Java counterpart from BigCloneBench

Input: 
    1. NiCad Clone in CSV format
    Directory,Filename_bc,StartLine_bc,Endline_bc,Directory,Filename_bc,StartLine_bc,Endline_bc
    2. BigCloneBench bc mapper in CSV format
    Directory,Filename, StartLine, EndLine, StartLine_bc, EndLine_bc, Filename_bc
Output: 
    BigCloneEval input, in the format
    Directory,Filename,StartLine,Endline,Directory,Filename,StartLine,Endline


How to use:
1. In the terminal run "python clone_mapper.py [code_clone_file_csv] [original_mapping] [output_file]"
2. if you enter 1 for modes, it will rename all file ending with class.bc to .java, otherwise by default file endings won't change

"""

def get_file_content(file_path):
    file_content = []
    with open(file_path, 'r') as file:
        line = file.readline()
        while line:
            line = line[:-1] # remove \n at the end
            file_content.append(line)
            line = file.readline()
    return file_content



def main():
    input_file_path = sys.argv[1]
    original_mapping_file_path = sys.argv[2]
    output_file_path = sys.argv[3]

    inputs = get_file_content(input_file_path)
    mappings = get_file_content(original_mapping_file_path)

if __name__ == "__main__":
    main()