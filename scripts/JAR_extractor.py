import os
import sys
print("Python path:", sys.path)
from util.file_counter import find_total_files_with_certain_file_ending
from util.file_walker import walk_with_specific_file_ending

def main():
    print('''
          ____________________________________________________________
          
          JAR_extractor
          ____________________________________________________________
          ''')
    
    
    print(os.getcwd())
    print(sys.argv[1])
    path = os.path.join(os.getcwd(), sys.argv[1])
    print(path)
    command = "jar -xf "
    file_ending = ".jar"
    total_files = find_total_files_with_certain_file_ending(file_ending, path)

    # Traverse through the directories(and subdirectories) in Java_Classes
    walk_with_specific_file_ending(path, command, file_ending, total_files)


if __name__ == "__main__":
    main()
