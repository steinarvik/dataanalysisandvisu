import os
from datetime import datetime

# Define the directory containing the files
directory = "files"

# Define the current date in the desired format
current_date = datetime.now().strftime("%Y-%m-%d")

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        # Construct the new filename by adding the current date
        new_filename = f"{filename[:-4]}-{current_date}.txt"
        # Construct the full file paths
        old_file_path = os.path.join(directory, filename)
        new_file_path = os.path.join(directory, new_filename)
        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed '{filename}' to '{new_filename}'")

print("File renaming completed.")