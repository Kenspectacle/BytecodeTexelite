import os
import subprocess
import sys
from util.file_counter import find_total_files_without_certain_file_ending
from util.file_walker import walk_with_filtered_file_ending

def main():
    print(os.getcwd())
    print(sys.argv[1])
    path = os.path.join(os.getcwd(), sys.argv[1])
    print(path)
    # Using the slash to escape $ characters
    command = "rm "
    file_ending = ".bc"
    total_files = find_total_files_without_certain_file_ending(file_ending, path)
    current_file_number = 0
    
    walk_with_filtered_file_ending(path, command, file_ending, total_files)
    

    # # Traverse through the directories(and subdirectories) in Java_Classes
    # for dirpath, dirs, files in os.walk(path):
    #     for file in files:
    #         if file.endswith(".bc"):
    #             print("File Progress: " + str(current_file_number) +
    #                 "/" + str(total_files))
    #             current_file_number += 1
    #             continue
    #         current_file_number += 1
    #         os.chdir(dirpath)
    #         print("File Progress: " + str(current_file_number) +
    #                 "/" + str(total_files))
    #         print(os.getcwd() + " " + file)
    #         subprocess.run(command + "'" + file + "'", shell=True,
    #                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


if __name__ == "__main__":
    main()
