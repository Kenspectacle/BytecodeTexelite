# BytecodeTexelite
Used to process all Java files into .class.bc Java Bytecode files. It works by extracting everything within the jar file, and then copying the class files into another folder, and finally getting the bytecode file.
## Requirement
Java 8+ installed
Python 3 installed
Running the script using Bash
## How to use to preprocess java bytecode file into .class.bc files
1. Use JAR_extractor.py and specify which folder to extract out the JAR files. The output will be in a folder named _[name] of the jar file
2. Use move_all_class_file_to_new_folder to move all of the class files outside of the extracted JAR folders
2.a.(OPTIONAL) Use delete_classfiles_with_dollar.py to remove class files duplicate with $ in its name
3. use class_file_to_text_bytecode.py to use the javap decompiler and created a text version of it using the -p flag. It makes the class files readable and adds the .bc extension at the end.
4. use remove_all_file_except_bc_files to remove the artifacts created that are not .class.bc files
5. use remove_empty_folders to remove the empty folders created by JAR_extractor
## Unwrapper for XML
This is used for preprocessing the code clone XML output from NiCad before it is used as an input to BigCloneBench. In order to use this, you simply need to run this command in your terminal

 ```
python code_clone_XML_unwrapper.py [code_clone_file] [output file]
 ```

## Bytecode Shortcut Unwrapper
In Bytecode files, it is common to use shortcuts for commonly used JVM instructions, such as aload_0 or aload_1. In the Bytecode shortcut unwrapper, you can unwrap the shortcut, such that the JVM instruction and the operator are separated. To use this, simply run
```
./Bytecode_Shortcut_Unwrapper.sh [target_folder]

```
Warning: This script will replace the original files.

## Known Bugs:
1. move_class_file_to_new_folder will skip files with "$" on their name
2. Running move_class_file_to_new_folder twice will move all of the class files to the home directory(!)