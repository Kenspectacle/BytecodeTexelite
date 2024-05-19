import os
import subprocess

def walk_with_filtered_directory(path, command, file_ending, filtered_directory, total_files):
        current_file_number = 0
        
        
        # Traverse through the directories(and subdirectories) in Java_Classes
        for dirpath, dirs, files in os.walk(path):
            
            # Calculate the relative path from the starting directory
            rel_path = os.path.relpath(dirpath, path)
            if filtered_directory in rel_path:
                        continue  # Skip this directory
                    
            for file in files:
                if file.endswith(file_ending):
                    # Check if the directory path contains "/StubClasses"
                    
                    current_file_number += 1
                    os.chdir(dirpath)
                    
                    # print file tracker
                    print("File Progress: " + str(current_file_number) +
                        "/" + str(total_files))
                    print(os.getcwd() + " " + file)
                    
                    subprocess.run(command + file + " ..", shell=True,
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)