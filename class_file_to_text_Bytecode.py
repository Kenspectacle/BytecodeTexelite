import os
import subprocess
import sys
from util.file_counter import find_total_files

def main():
    print(os.getcwd())
    path = os.path.join(os.getcwd(), sys.argv[1])
    file_ending = ".class"
    filtered_directory = "StubClass"
    total_files = find_total_files(file_ending, path, filtered_directory)
    command = "javap -c "
    current_file_number = 0

    # Traverse through the directories(and subdirectories) in Java_Classes
    for dirpath, dirs, files in os.walk(path):
        for file in files:
            dirname = dirpath.split(os.path.sep)[-1]
            if file.endswith(".class") and dirname != "StubClass":
                current_file_number += 1
                os.chdir(dirpath) # Change working directory to dirpath
                result = subprocess.run(
                    command + file, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                print("File Progress: " + str(current_file_number) +
                      "/" + str(total_files))
                print(os.getcwd() + " " + file)
                # Write out the output file of stdout
                with open(os.path.join(os.path.dirname(dirpath), f"{file}.bc"), "w") as f:
                    f.write(result.stdout)


if __name__ == "__main__":
    main()
