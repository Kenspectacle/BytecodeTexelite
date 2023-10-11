import os
import subprocess


def findTotalFiles():
    path = os.getcwd() + "/Java_Classes"
    total_files = 0
    for dirpath, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".jar"):
                total_files += 1
    return total_files


def main():
    print(os.getcwd())
    path = os.getcwd() + "/Java_Classes"
    command = "jar -xf "
    total_files = findTotalFiles()
    current_file_number = 0

    # Traverse through the directories(and subdirectories) in Java_Classes
    for dirpath, dirs, files in os.walk(path):
        # Calculate the relative path from the starting directory
        rel_path = os.path.relpath(dirpath, path)
        for file in files:
            if file.endswith(".jar"):
                current_file_number += 1
                os.chdir(dirpath)
                print("File Progress: " + str(current_file_number) +
                    "/" + str(total_files))
                print(os.getcwd() + " " + file)
                subprocess.run(command + file, shell=True,
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


if __name__ == "__main__":
    main()
