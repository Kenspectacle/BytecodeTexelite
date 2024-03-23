import sys
import re

"""

"""


def get_subdirectory(directory):
    subdirectory = ""
    
    return subdirectory




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
