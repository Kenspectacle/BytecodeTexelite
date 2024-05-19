import os

# Find all of the files
def find_total_files(path):
    total_files = 0
    
    for dirpath, dirs, files in os.walk(path):
        for file in files:
            total_files += 1
            
    return total_files

# Find all of the files with a certain file ending
def find_total_files_with_certain_file_ending(file_ending, path):
    total_files = 0
    
    for dirpath, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(file_ending):
                total_files += 1
                
    return total_files

# Find all of the files without a certain file ending
def find_total_files_without_certain_file_ending(file_ending, path):
    total_files = 0
    for dirpath, dirs, files in os.walk(path):
        for file in files:
            
            if file.endswith(file_ending):
                continue
            else:
                total_files += 1
                
    return total_files

# Find all of the files with a certain file ending while filtering out a directory
def find_total_files_with_file_ending_and_filtered_directory(file_ending, path, filtered_directory):
    total_files = 0
    
    for dirpath, dirs, files in os.walk(path):
        
        # Find the relative path and filter all the directory that is in the relative path
        rel_path = os.path.relpath(dirpath, path)
        if filtered_directory in rel_path:
                    continue  # Skip this directory
                
        for file in files:
            if file.endswith(file_ending):
                total_files += 1
                
    return total_files