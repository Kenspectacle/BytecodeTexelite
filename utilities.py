import os

# Find all of the file with a certain file ending
def find_total_files(file_ending, path):
    total_files = 0
    for dirpath, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(file_ending):
                total_files += 1
    return total_files

# Find all of the file with a certain file ending while filtering out a directory
def find_total_files(file_ending, path, filtered_directory):
    total_files = 0
    for dirpath, dirs, files in os.walk(path):
        # Ignores StubClass folder
        dirname = dirpath.split(os.path.sep)[-1]
        for file in files:
            if file.endswith(file_ending) and dirname != filtered_directory:
                total_files += 1
    return total_files