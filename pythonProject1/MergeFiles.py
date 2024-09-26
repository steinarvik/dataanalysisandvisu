import glob
import os

# Folder containing the text files
folder_path = 'Texter'

# Pattern to match all .txt files in the folder
pattern = os.path.join(folder_path, '*.txt')

# New file to store the merged content
merged_file_path = '../merged_file.txt'

# List to hold the content of each text file
merged_content = []

# Use glob to find all files matching the pattern, and sort them alphabetically
file_paths = sorted(glob.glob(pattern))

# Iterate through each sorted file path
for file_path in file_paths:
    # Open and read the file's content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Add the content to the list
        merged_content.append(content)

# Open the new file in write mode
with open(merged_file_path, 'w', encoding='utf-8') as merged_file:
    # Write each file's content into the merged file
    for content in merged_content:
        merged_file.write(content + "\n")  # Adding a newline for separation

print("Merging completed. All text files have been merged into:", merged_file_path)