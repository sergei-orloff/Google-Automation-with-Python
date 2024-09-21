#!/usr/bin/env python3

import sys
import os
import subprocess


def main():
    # Check if the oldFiles.txt path is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python3 changeJane.py <path_to_oldFiles.txt>")
        sys.exit(1)

    # Open the oldFiles.txt file
    with open(sys.argv[1], 'r') as file:
        # Read all lines from the file
        lines = file.readlines()

    # Process the lines in groups of three
    for i in range(2, len(lines), 3):
        old_name = lines[i].strip()

        # Update the path to look in /home/student/data/
        full_old_path = os.path.join('/home/student/data', os.path.basename(old_name))

        if os.path.exists(full_old_path):
            # Replace 'jane' with 'jdoe' in the filename
            new_name = os.path.basename(old_name).replace('jane', 'jdoe')
            full_new_path = os.path.join('/home/student/data', new_name)

            # Use subprocess to rename the file
            print(f"Renaming {full_old_path} to {full_new_path}")
            subprocess.run(['mv', full_old_path, full_new_path])
        else:
            print(f"File not found: {full_old_path}")

    # Check for any additional 'jane' files that weren't in oldFiles.txt
    for filename in os.listdir('/home/student/data'):
        if 'jane' in filename.lower():
            old_path = os.path.join('/home/student/data', filename)
            new_name = filename.replace('jane', 'jdoe').replace('Jane', 'Jdoe')
            new_path = os.path.join('/home/student/data', new_name)
            print(f"Additional file found. Renaming {old_path} to {new_path}")
            subprocess.run(['mv', old_path, new_path])

    print("File processing complete.")


if __name__ == "__main__":
    main()