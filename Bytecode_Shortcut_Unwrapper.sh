#!/bin/sh

TARGET_FOLDER="$1"

# Use find command to list all files recursively in the target folder
find "$TARGET_FOLDER" -type f | while read -r file; do
    # Use sed to unwrap the shortcut
    sed -i 's/\([a-zA-Z_][a-zA-Z_0-9]*\)_\([0-9]\{1,\}\)/\1 \2/; s/iconst_m1/iconst -1/' "$file"
done

