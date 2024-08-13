import os
import sys
import subprocess

def main():
    
    print('''
          ____________________________________________________________
          
          move_class_file_to_new_folder
          ____________________________________________________________
          ''')
    
    # metadata
    print(os.getcwd())
    path = os.path.join(os.getcwd(), sys.argv[1])
    file_ending = ".class"
    filtered_directory = "StubClass"
    current_file_number = 0
    # find total files
    
    # execute the script
    # Traverse through the directories(and subdirectories) in Java_Classes
    for dirpath, dirs, files in os.walk(path):
        
        # Calculate the relative path from the starting directory
        rel_path = os.path.relpath(dirpath, path)
        if filtered_directory in rel_path:
                print("TEST")

                continue  # Skip this directory

        parent_folder_name = os.path.basename(dirpath)
        javaname = parent_folder_name[1:] # remove the _ behind the name        
        for file in files:
            if file.endswith(file_ending):                
                current_file_number += 1
                os.chdir(dirpath)
                
                # print file tracker
                new_file_name = f"{javaname}_{file}"
                print(f"File Progress: {current_file_number}/{0}")
                print(f"Renaming and moving {os.path.join(dirpath, file)} to {new_file_name}")
                result = subprocess.run(f"mv {file} ../{new_file_name}", shell=True, cwd=dirpath, text=True,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    


if __name__ == "__main__":
    main()
