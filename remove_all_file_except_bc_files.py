import os
import sys
from util.file_counter import find_total_files_without_certain_file_ending
from util.file_walker import walk_with_filtered_file_ending_and_escaped_files

def main():
    print(os.getcwd())
    print(sys.argv[1])
    path = os.path.join(os.getcwd(), sys.argv[1])
    print(path)
    command = "rm "
    file_ending = ".bc"
    total_files = find_total_files_without_certain_file_ending(file_ending, path)
    
    walk_with_filtered_file_ending_and_escaped_files(path, command, file_ending, total_files)

if __name__ == "__main__":
    main()
