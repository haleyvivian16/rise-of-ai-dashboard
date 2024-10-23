import pandas as pd

# Load the dataset
df = pd.read_csv('rise_of_ai.csv')  # Replace with your actual filename

# Display the first few rows of the dataset
print(df.head())

# Data cleaning (if needed)
# Example: Remove any unnecessary whitespace or special characters
df.columns = df.columns.str.strip()  # Strip whitespace from column names

# Convert numerical columns to appropriate data types (remove '$' and convert to float)
df['AI Software Revenue'] = df['AI Software Revenue'].replace(
    {'\$': '', ',': ''}, regex=True).astype(float)
df['Global AI Market Value'] = df['Global AI Market Value'].replace(
    {'\$': '', ',': ''}, regex=True).astype(float)

# Check for missing values
print(df.isnull().sum())
