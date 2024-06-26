#!/bin/sh

TARGET_FOLDER="$(realpath $1)"
SCRIPT_FOLDER="$(realpath ./scripts)"
UTIL_FOLDER="$(realpath ./util)"

# Set the PYTHONPATH to include the util directory
export PYTHONPATH="./"

# Debug: print the PYTHONPATH
echo "PYTHONPATH is set to: $PYTHONPATH"
echo "TARGET_FOLDER: $TARGET_FOLDER"
echo "SCRIPT_FOLDER: $SCRIPT_FOLDER"
echo "UTIL_FOLDER: $UTIL_FOLDER"

# Run all of the scripts in bytecode texelite with the SCRIPT_FOLDER as a prefix
python "$SCRIPT_FOLDER/JAR_extractor.py" $TARGET_FOLDER
python "$SCRIPT_FOLDER/move_class_file_to_new_folder.py" $TARGET_FOLDER
python "$SCRIPT_FOLDER/delete_classfiles_with_dollar.py" $TARGET_FOLDER
python "$SCRIPT_FOLDER/class_file_to_text_Bytecode.py" $TARGET_FOLDER
python "$SCRIPT_FOLDER/remove_all_file_except_bc_files.py" $TARGET_FOLDER
python "$SCRIPT_FOLDER/remove_empty_folders.py" $TARGET_FOLDER
