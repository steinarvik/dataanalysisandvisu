import pandas as pd

# Step 2: Load Data
sales_data = pd.read_excel('input.xlsx')

# Step 3: Explore Data
print(sales_data.head())
print(sales_data.info())
print(sales_data.describe())

# Step 4: Data Cleaning (Example: Handling missing values)
sales_data.dropna(inplace=True)

# Step 5: Add Profit column
sales_data['Total'] = sales_data['Price'] * sales_data['Quantity']

# Step 6: Save updated DataFrame to a new Excel file
sales_data.to_excel('output.xlsx', index=False)

print("New Excel file saved successfully.")