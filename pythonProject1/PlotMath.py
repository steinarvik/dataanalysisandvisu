import os
import matplotlib.pyplot as plt

# Define the directory containing the text files
directory = "files"

# Initialize a list to hold the numbers
numbers = []
file_names = []

# Loop through each file in the directory
for filename in sorted(os.listdir(directory)):
    if filename.endswith(".txt"):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r') as file:
            # Read the number from the file and convert it to float
            number = float(file.read().strip())
            numbers.append(number)
            file_names.append(filename[:-4])  # Remove .txt extension for the plot

# Plotting the numbers
plt.figure(figsize=(10, 6))
plt.plot(file_names, numbers, marker='o', linestyle='-', color='b')
plt.title('Numbers from Text Files')
plt.xlabel('File Name')
plt.ylabel('Number')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()