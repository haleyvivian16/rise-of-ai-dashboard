import pandas as pd

# Clean percentage columns by removing '%' and converting to float
def clean_percentage_column(df, column_name):
    # Convert column to string first to handle percentage removal
    df[column_name] = df[column_name].astype(str).str.replace('%', '').astype(float)
    return df

# Clean monetary columns by removing '$' and ',' and converting to float
def clean_monetary_column(df, column_name):
    # Only perform string operations if the column contains strings
    if df[column_name].dtype == 'object':
        df[column_name] = df[column_name].str.replace(r'[$,]', '', regex=True).astype(float)
    return df

# Load the dataset
input_file = 'rise_of_ai.csv' 
df = pd.read_csv(input_file)

# Clean monetary columns 
monetary_columns = [
    'AI Software Revenue(in Billions)',  
    'Global AI Market Value(in Billions)', 
    'AI Contribution to Healthcare(in Billions)',  
    'Estimated Revenue Increase from AI (trillions USD)'  
]
for col in monetary_columns:
    df = clean_monetary_column(df, col)

# Clean percentage columns 
percentage_columns = [
    'AI Adoption (%)', 
    'Organizations Using AI', 
    'Organizations Planning to Implement AI', 
    'Global Expectation for AI Adoption (%)',  
    'Net Job Loss in the US', 
    'Organizations Believing AI Provides Competitive Edge', 
    'Companies Prioritizing AI in Strategy', 
    'Marketers Believing AI Improves Email Revenue', 
    'Americans Using Voice Assistants (%)', 
    'Medical Professionals Using AI for Diagnosis', 
    'Jobs at High Risk of Automation - Transportation & Storage (%)',  
    'Jobs at High Risk of Automation - Wholesale & Retail Trade', 
    'Jobs at High Risk of Automation - Manufacturing'
]
for col in percentage_columns:
    df = clean_percentage_column(df, col)

# Save the cleaned dataset to a new CSV file
output_file = 'cleaned_rise_of_ai.csv'
df.to_csv(output_file, index=False)

print(f'Data cleaning complete. Cleaned data saved to {output_file}.')

