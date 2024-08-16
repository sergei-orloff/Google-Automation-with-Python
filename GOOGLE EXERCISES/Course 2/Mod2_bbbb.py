import os


def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, 'w') as f:
        f.write(comments)
        filesize = f.tell()
    return filesize


print(create_python_script("program.py"))

# ===================================


def new_directory(directory, filename):
    # Before creating a new directory, check if it already exists
    if not os.path.isdir(directory):  # Check if directory doesn't exist
        os.mkdir(directory)  # Create the directory if it doesn't exist

    # Change directory to the newly created directory
    os.chdir(directory)  # Adjust if you need to operate within the directory

    # Create the new file inside the new directory
    with open(filename, 'w') as file:
        pass  # No need to write anything to create the file

    os.chdir('..')  # Go back to the parent directory if needed
    # Return the list of files in the new directory
    return os.listdir(directory)


print(new_directory("PythonPrograms", "script.py"))

# ================================

import datetime


def file_date(filename):
    # Create the file in the current directory
    open(filename, 'w').close()

    # Get the timestamp of the file's modification time
    timestamp = os.path.getmtime(filename)

    # Convert the timestamp into a readable format, then into a string
    date_time_obj = datetime.datetime.fromtimestamp(timestamp)

    # Return just the date portion
    return date_time_obj.strftime("%Y-%m-%d")


print(file_date("newfile.txt"))
