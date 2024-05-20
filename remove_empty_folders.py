import os
import sys

path = os.path.join(os.getcwd(), sys.argv[1])

def remove_empty_subfolders(path):
    # Traverse the directory tree from bottom to top
    for dirpath, dirnames, filenames in os.walk(path, topdown=False):
        # Remove empty directories
        for dirname in dirnames:
            dir_to_check = os.path.join(dirpath, dirname)
            print(dir_to_check)
            print(os.listdir(dir_to_check))
            if not os.listdir(dir_to_check):  # Check if directory is empty
                os.rmdir(dir_to_check)
                print(f"Removed empty directory: {dir_to_check}")

remove_empty_subfolders(path)