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

class CloneMappingError(Exception):
    """Exception raised for errors in the clone mapping process."""
    def __init__(self, message="Clone mapping not found"):
        self.message = message
        super().__init__(self.message)

def get_file_content(file_path):
    file_content = []
    with open(file_path, 'r') as file:
        line = file.readline()
        while line:
            line = line[:-1] # remove \n at the end
            file_content.append(line)
            line = file.readline()
    return file_content

def extract_input_data(input_data):
    directory = input_data[0]
    filename_bc = input_data[1]
    startline_bc = int(input_data[2])
    endline_bc = int(input_data[3])
    directory_2 = input_data[4]  
    filename_bc_2 = input_data[5]
    startline_bc_2 = int(input_data[6])
    endline_bc_2 = int(input_data[7])
    return directory, filename_bc, startline_bc, endline_bc, directory_2, filename_bc_2, startline_bc_2, endline_bc_2

def extract_mapping_data(mapping_data):
    directory_mapper = mapping_data[0]
    filename_java = mapping_data[1]
    startline_java = int(mapping_data[2])
    endline_java = int(mapping_data[3])
    startline_bc_mapper = int(mapping_data[4])
    endline_bc_mapper = int(mapping_data[5])
    filename_bc_mapper = mapping_data[6]
    return directory_mapper, filename_java, startline_java, endline_java, startline_bc_mapper, endline_bc_mapper, filename_bc_mapper

def within_tolerance(value, target, tolerance=2):
    return target - tolerance <= value <= target + tolerance


def map_output(inputs, mappings):
    outputs = []
    for input in inputs:
        first_clone_map_found = False
        second_clone_map_found = False

        print(input)
        # extract the input
        input_data = input.split(',')
        directory, filename_bc, startline_bc, endline_bc, directory_2, filename_bc_2, startline_bc_2, endline_bc_2 = extract_input_data(input_data)

        print(f'''
processing current input
directory: {directory}
filename_bc: {filename_bc}
startline_bc: {startline_bc}
endline_bc: {endline_bc}
directory_2: {directory_2}
filename_bc_2: {filename_bc_2}
startline_bc_2: {startline_bc_2}
endline_bc_2: {endline_bc_2}
        ''')
        
        for mapping in mappings:

            if first_clone_map_found and second_clone_map_found:
                break

            mapping_data = mapping.split(',')
            directory_mapper, filename_java, startline_java, endline_java, startline_bc_mapper, endline_bc_mapper, filename_bc_mapper = extract_mapping_data(mapping_data)
            
            # check for clone 1
            if (
                directory == directory_mapper
                and filename_bc == filename_bc_mapper
                and within_tolerance(startline_bc, startline_bc_mapper)
                and within_tolerance(endline_bc, endline_bc_mapper)
            ):
                print('Clone 1 mapping found!')
                print(f'Transforming from: {filename_bc}, {startline_bc}, {endline_bc} to {filename_java}, {startline_java}, {endline_java}')
                first_clone_map_found = True
            
            # Check for clone 2
            if (
                directory_2 == directory_mapper
                and filename_bc_2 == filename_bc_mapper
                and within_tolerance(startline_bc_2, startline_bc_mapper)
                and within_tolerance(endline_bc_2, endline_bc_mapper)
            ):
                print('Clone 2 mapping found!')
                print(f'Transforming from: {filename_bc_2}, {startline_bc_2}, {endline_bc_2} to {filename_java}, {startline_java}, {endline_java}')
                second_clone_map_found = True
        
        # case: one of the clone can't find any mapping
        if not first_clone_map_found or not second_clone_map_found:
            raise CloneMappingError()


    return outputs


def main():
    input_file_path = sys.argv[1]
    original_mapping_file_path = sys.argv[2]
    output_file_path = sys.argv[3]

    inputs = get_file_content(input_file_path)
    mappings = get_file_content(original_mapping_file_path)
    outputs = map_output(inputs, mappings)

if __name__ == "__main__":
    main()