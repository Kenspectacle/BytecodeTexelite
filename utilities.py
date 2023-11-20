import os


def find_total_files(fileEnding, path):
    total_files = 0
    for dirpath, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(fileEnding):
                total_files += 1
    return total_files