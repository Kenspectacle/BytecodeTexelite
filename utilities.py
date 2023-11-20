import os


def find_total_files(file_ending, path):
    total_files = 0
    for dirpath, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(file_ending):
                total_files += 1
    return total_files