# Rename Multiple Files
# Reference: https://learnpython.com/blog/how-to-rename-files-python/

# import
from pathlib import Path
 
# directory path
path = Path.cwd() / 'DIRECTORY FOLDER LOCATION (/)'
 
# initiate counter
count = 1
 
# loop through the directory and rename the files
for file in path.iterdir():
    if file.is_file():
        prefix = "EXPECTED FILE NAME" # new file name
        counter = str(count).zfill(0) # file numbers and set the number of digits
        file_extension = file.suffix 

        rename = prefix + counter + file_extension # renaming

        file.rename(path / rename) # file destination
        count += 1