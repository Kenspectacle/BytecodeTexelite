#!/bin/sh

TARGET_FOLDER="$1"

# run all of the scripts in bytecode texelite
python JAR_extractor.py $TARGET_FOLDER
python move_class_file_to_new_folder.py $TARGET_FOLDER
python delete_classfiles_with_dollar.py $TARGET_FOLDER
python class_file_to_text_Bytecode.py $TARGET_FOLDER
python remove_all_file_except_bc_files.py $TARGET_FOLDER
python remove_empty_folders.py $TARGET_FOLDER