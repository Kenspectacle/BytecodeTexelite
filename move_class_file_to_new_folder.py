import os
import sys
from util.file_counter import find_total_files_with_file_ending_and_filtered_directory
from util.file_walker import walk_with_filtered_directory

def main():
    
    # metadata
    print(os.getcwd())
    path = os.path.join(os.getcwd(), sys.argv[1])
    command = "mv "
    file_ending = ".class"
    filtered_directory = "StubClass"
    
    # find total files
    total_files = find_total_files_with_file_ending_and_filtered_directory(file_ending, path, filtered_directory)
    
    # execute the script
    walk_with_filtered_directory(path, command, file_ending, filtered_directory, total_files)
    


if __name__ == "__main__":
    main()
