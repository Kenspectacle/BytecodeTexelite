import sys
import re

"""
This is a file used for preprocessing the code clones output 
from NiCad Clone Detector, to be used as an input to BigCloneEval

Input: 
    NiCad Clone xml report file
Output: 
    BigCloneEval input, in the format
    Directory,Filename,StartLine,Endline,Directory,Filename,StartLine,Endline


How to use:
1. Use NiCad to create code clones
2. Take one of the file from the output in NiCad
3. In the terminal run "python code_clone_XML_unwrapper.py [code_clone_file]"

"""

# Separate the directory and file in path
def separate_directory_and_file(path):
    # Define the regex pattern
    pattern = r'^(.*[\\\/])(.*)$'  # Matches the directory part and the file part
    
    # Match the pattern against the path
    match = re.match(pattern, path)
    
    # Extract directory and file name if there's a match
    if match:
        directory = match.group(1)
        filename = match.group(2)
        return directory, filename
    else:
        return "default", path

# Extract the metadata from <source>
def source_extractor(source):
    directory = ""
    filename = ""
    startline = ""
    endline = ""
    print("Source: ", source)
    splitted_source = source.split(" ")
    path_with_stringlit = splitted_source[1][5:]
    
    # Get Path
    path = path_with_stringlit[1:len(path_with_stringlit) - 1]
    print("path: ", path)
    
    # Separate Directory and Filename from path
    directory,filename = separate_directory_and_file(path)
    print("directory: ", directory)
    print("filename: ", filename)
    
    # Get Startline
    startline = splitted_source[2][11:]
    startline = startline[0:len(startline) - 1]
    print("startline: ", startline)
    
    # Get Endline
    endline = splitted_source[3][9:]
    endline = endline[0:len(endline) - 1]
    print("endline: ", endline)
    
    return directory,filename,startline,endline






def main():
    outputs = []
    
    # Takes the first arg as the file input 
    print(sys.argv[1])
    
    
    # Open a code clone xml result from NiCad
    with open(sys.argv[1], 'r') as file:
        # Read the first line
        line = file.readline()
        print(line)
        
        # Iterate through the rest
        while line:
            print(line)
            # Find Clone pair
            if line[0:7] == "<clone ":
                print('CLONE: ', line)
                
                # prepare output
                output = ""
                
                # first clone source
                line = file.readline()
                directory1,filename1,startline1,endline1 = source_extractor(line)
                
                 # second clone source
                line = file.readline()
                directory2,filename2,startline2,endline2 = source_extractor(line)
                
                # add into outputs list
                output = directory1 + "," + filename1 + ',' + startline1 + ',' + endline1 + ',' + directory2 + "," + filename2 + ',' + startline2 + ',' + endline2
                outputs.append(output)
            
            line = file.readline()

    # To check the outputs as debugging log
    print("Result of the output: ")
    for output in outputs:
        print(output)
        
    # Write a new file as the output
    with open(sys.argv[2], 'w') as file:
        for output in outputs:
            file.write(output + "\n")

if __name__ == "__main__":
    main()