import os
import subprocess
import sys
from util.file_counter import find_total_files_with_file_ending_and_filtered_directory

def main():
    print(os.getcwd())
    path = os.path.join(os.getcwd(), sys.argv[1])
    file_ending = ".class"
    filtered_directory = "StubClass"
    total_files = find_total_files_with_file_ending_and_filtered_directory(file_ending, path, filtered_directory)
    command = "javap -c "
    current_file_number = 0

    # Traverse through the directories(and subdirectories) in Java_Classes
    for dirpath, dirs, files in os.walk(path):
        
        # Calculate the relative path from the starting directory
        rel_path = os.path.relpath(dirpath, path)
        if filtered_directory in rel_path:
            continue  # Skip this directory
        
        for file in files:
                    
            if file.endswith(".class"):
                current_file_number += 1
                os.chdir(dirpath) # Change working directory to dirpath
                
                # get the result of the command
                result = subprocess.run(
                    command + file, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                
                print(f"File Progress: {current_file_number}/{total_files}")
                print(f"Processing {os.path.join(os.getcwd(), file)}")

                # Write the output of stdout to a .bc file in the same directory
                output_file = os.path.join(dirpath, f"{os.path.splitext(file)[0]}.bc")
                with open(output_file, "w") as f:
                    f.write(result.stdout)


if __name__ == "__main__":
    main()
