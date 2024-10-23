import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('rise_of_ai.csv')  

# Display the initial data and column names for debugging
print("Initial Data:")
print(df.head())
print("\nColumn Names:")
print(df.columns.tolist())

# Data Cleaning and Conversion
# Clean 'AI Software Revenue(in Billions)' and 'Global AI Market Value(in Billions)' columns
df['AI Software Revenue(in Billions)'] = df['AI Software Revenue(in Billions)'].replace({r'\$': '', ',': ''}, regex=True).astype(float)
df['Global AI Market Value(in Billions)'] = df['Global AI Market Value(in Billions)'].replace({r'\$': '', ',': ''}, regex=True).astype(float)

# Clean 'Net Job Loss in the US' column by removing '%' sign and converting to float
df['Net Job Loss in the US'] = df['Net Job Loss in the US'].replace({r'%': '', ',': ''}, regex=True).astype(float)

# Clean percentage columns by removing '%' sign for other relevant columns
df['Jobs at High Risk of Automation - Manufacturing'] = df['Jobs at High Risk of Automation - Manufacturing'].replace({r'%': '', ',': ''}, regex=True).astype(float)
df['Jobs at High Risk of Automation - Transportation & Storage (%)'] = df['Jobs at High Risk of Automation - Transportation & Storage (%)'].replace({r'%': '', ',': ''}, regex=True).astype(float)

# Print the cleaned DataFrame to verify changes
print("\nCleaned Data:")
print(df.head())

# Example of creating an interactive plot using Plotly
fig = px.line(df, x='Year', y='AI Software Revenue(in Billions)',
              title='AI Software Revenue Over the Years',
              labels={'AI Software Revenue(in Billions)': 'AI Software Revenue (in Billions)', 'Year': 'Year'})
fig.show()

# Save the cleaned DataFrame for further use
df.to_csv('cleaned_rise_of_ai.csv', index=False)  # Optional: save cleaned data to a new CSV file
