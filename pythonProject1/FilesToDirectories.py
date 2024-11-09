import glob
import os
import shutil

# Dictionary to map file extensions to folder names
EXTENSION_MAP = {
    'txt': 'Text Files',
    'jpg': 'Images',
    'png': 'Images',
    'pdf': 'PDFs',
    'docx': 'Word Documents',
    'xlsx': 'Excel Files',
    'exe':  'Program files'
}


def organize_directory(directory):
    # Iterate over all files in the directory
    for ext, folder_name in EXTENSION_MAP.items():
        # Use glob to find files with the current extension
        pattern = os.path.join(directory, f'*.{ext}')
        for file_path in glob.glob(pattern):
            # Create the folder if it doesn't exist
            folder_path = os.path.join(directory, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Move the file to the corresponding folder
            shutil.move(file_path, folder_path)
            print(f'Moved: {os.path.basename(file_path)} -> {folder_name}')

    # Handle files that don't match any extension in EXTENSION_MAP
    other_files_pattern = os.path.join(directory, '*.*')
    for file_path in glob.glob(other_files_pattern):
        # Skip files already moved to categorized folders
        if not os.path.isfile(file_path):
            continue

        file_extension = file_path.split('.')[-1].lower()
        if file_extension not in EXTENSION_MAP:
            folder_path = os.path.join(directory, 'Other Files')
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            shutil.move(file_path, folder_path)
            print(f'Moved: {os.path.basename(file_path)} -> Other Files')


# Call the functions
target_directory = input("Enter the directory to organize: ")
organize_directory(target_directory)
print("Directory organized successfully!")