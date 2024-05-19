import os
import subprocess
import sys
from util.file_counter import find_total_files_with_file_ending_and_filtered_directory


def main():
    print(os.getcwd())
    path = os.path.join(os.getcwd(), sys.argv[1])
    command = "cp "
    file_ending = ".class"
    filtered_directory = "StubClass"
    total_files = find_total_files_with_file_ending_and_filtered_directory(file_ending, path, filtered_directory)
    current_file_number = 0

    # Traverse through the directories(and subdirectories) in Java_Classes
    for dirpath, dirs, files in os.walk(path):
        
        # Calculate the relative path from the starting directory
        rel_path = os.path.relpath(dirpath, path)
        if filtered_directory in rel_path:
                    continue  # Skip this directory
                
        for file in files:
            if file.endswith(".class"):
                # Check if the directory path contains "/StubClasses"
                
                current_file_number += 1
                os.chdir(dirpath)
                
                # print file tracker
                print("File Progress: " + str(current_file_number) +
                    "/" + str(total_files))
                print(os.getcwd() + " " + file)
                
                subprocess.run(command + file + " ..", shell=True,
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


if __name__ == "__main__":
    main()
