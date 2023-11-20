import os
import subprocess
import sys

def findTotalFiles(fileEnding, path):
    total_files = 0
    for dirpath, dirs, files in os.walk(path):
        # Ignores StubClass folder
        dirname = dirpath.split(os.path.sep)[-1]
        for file in files:
            if file.endswith(fileEnding) and dirname != "StubClass":
                total_files += 1
    return total_files


def main():
    print(os.getcwd())
    path = os.path.join(os.getcwd(), sys.argv[1])
    file_ending = ".class"
    total_files = findTotalFiles(file_ending, path)
    command = "javap -c "
    current_file_number = 0

    # Traverse through the directories(and subdirectories) in Java_Classes
    for dirpath, dirs, files in os.walk(path):
        for file in files:
            dirname = dirpath.split(os.path.sep)[-1]
            if file.endswith(".class") and dirname != "StubClass":
                current_file_number += 1
                os.chdir(dirpath)
                result = subprocess.run(
                    command + file, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                # print("Standard Output:")
                # print(result.stdout)
                # print("##########")
                print("File Progress: " + str(current_file_number) +
                      "/" + str(total_files))
                print(os.getcwd() + " " + file)
                # Write out the output file of stdout
                with open(os.path.join(os.path.dirname(dirpath), f"{file}.bc"), "w") as f:
                    f.write(result.stdout)


if __name__ == "__main__":
    main()
