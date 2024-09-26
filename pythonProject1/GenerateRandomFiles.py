import pandas as pd
from faker import Faker
import os

# Create a Faker instance
fake = Faker()

# Directory to save the generated Excel files
output_dir = "generated_excel_files"
os.makedirs(output_dir, exist_ok=True)

# Number of Excel files to generate
num_files = 100

# Function to generate random data
def generate_random_data(num_entries=50):
    data = {
        "Name": [fake.name() for _ in range(num_entries)],
        "Age": [fake.random_int(min=18, max=80) for _ in range(num_entries)],
        "Email": [fake.email() for _ in range(num_entries)]
    }
    return pd.DataFrame(data)

# Generate and save Excel files
for i in range(1, num_files + 1):
    df = generate_random_data()
    file_path = os.path.join(output_dir, f"random_data_{i}.xlsx")
    df.to_excel(file_path, index=False)
    print(f"Generated {file_path}")

print(f"Successfully generated {num_files} Excel files in the '{output_dir}' directory.")