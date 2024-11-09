import os
import glob

def search_files(directory, search_term):
    # Search for files matching the search term in the specified directory
    search_pattern = os.path.join(directory, f"*{search_term}*")
    matching_files = glob.glob(search_pattern)

    if matching_files:
        print("Files matching your search:")
        for file_path in matching_files:
            print(file_path)
    else:
        print("No matching files found.")


if __name__ == "__main__":
    directory = input("Enter the directory to search in: ")
    search_term = input("Enter the search term or file extension (e.g., '.txt'): ")

    # Validate directory
    if os.path.isdir(directory):
        search_files(directory, search_term)
    else:
        print("Invalid directory. Please try again.")