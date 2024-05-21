import os
import subprocess
import sys
from util.file_counter import find_total_files_with_certain_keyword

def main():
    print(os.getcwd())
    path = os.path.join(os.getcwd(), sys.argv[1])
    file_ending = ".class"
    filtered_directory = "StubClass"
    keyword = "$"
    total_files = find_total_files_with_certain_keyword(file_ending, path, keyword)
    command = "rm "
    current_file_number = 0

    # Traverse through the directories(and subdirectories) in Java_Classes
    for dirpath, dirs, files in os.walk(path):
        
        # Calculate the relative path from the starting directory
        rel_path = os.path.relpath(dirpath, path)
        if filtered_directory in rel_path:
            continue  # Skip this directory
        
        for file in files:
                    
            if file.endswith(".class") and keyword in file:
                current_file_number += 1
                os.chdir(dirpath) # Change working directory to dirpath
                
                # Quote the filename to handle special characters
                quoted_file = "'" + file.replace("'", "'\\''") + "'"
                
                subprocess.run(command + quoted_file, shell=True,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                
                print(f"File Progress: {current_file_number}/{total_files}")
                print(f"Processing {os.path.join(os.getcwd(), file)}")
                


if __name__ == "__main__":
    main()
