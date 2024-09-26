import os
import pandas as pd
import streamlit as st

# Define the directory containing the text files
directory = "files"

# Initialize a list to hold the numbers and file names
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
            file_names.append(filename[:-4])  # Remove .txt extension for display

# Create a DataFrame for Streamlit plotting
data = pd.DataFrame({
    'File Names': file_names,
    'Numbers': numbers
})

# Use Streamlit to plot the numbers
st.title('Numbers from Text Files')

# Plotting with custom x-axis labels
st.line_chart(data.set_index('File Names'))

# Displaying filenames and corresponding numbers below the chart for reference
st.write("File Names and their Corresponding Numbers:")
for name, num in zip(file_names, numbers):
    st.write(f"{name}: {num}")