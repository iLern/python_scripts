import os
import re

"""
This script is used to modify the creation date of all files 
in this directory and its subdirectories 
to the date represented by their file name.

NOTICE: command `setfile` only work on MacOS
"""

# Define a regular expression pattern to match the filename format "YYYY-M-D"
pattern = re.compile(r'^(\d{4})-(\d{1,2})-(\d{1,2}).md$')

# Iterate over all files in the current directory and its subdirectories
for dirpath, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        # Check if the filename matches the pattern
        match = pattern.match(filename)
        if match:
            # Extract the year, month, and day from the filename
            year, month, day = match.groups()

            # Get the full path of the file
            filepath = os.path.join(dirpath, filename)

            # Use the SetFile command to set the creation time of the file
            os.system(f'setfile -d "{month}/{day}/{year} 00:00:00" "{filepath}"')
