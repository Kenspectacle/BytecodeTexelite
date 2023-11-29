import os
import subprocess
import sys
from utilities import find_total_files


def main():
    print(os.getcwd())
    print(sys.argv[1])
    path = os.path.join(os.getcwd(), sys.argv[1])
    print(path)
    # Using the slash to escape $ characters
    command = "rm "
    total_files = find_total_files(path)
    current_file_number = 0

    # Traverse through the directories(and subdirectories) in Java_Classes
    for dirpath, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".bc"):
                print("File Progress: " + str(current_file_number) +
                    "/" + str(total_files))
                current_file_number += 1
                continue
            current_file_number += 1
            os.chdir(dirpath)
            print("File Progress: " + str(current_file_number) +
                    "/" + str(total_files))
            print(os.getcwd() + " " + file)
            subprocess.run(command + "'" + file + "'", shell=True,
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


if __name__ == "__main__":
    main()
