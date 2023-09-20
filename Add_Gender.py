import pandas as pd

# Define the file path
file_path = 'C:/CCLAMP_gender/C-CLAMP_metadata.txt'

# Define the column names
columns = ['File', 'Year', 'Title', 'Author', 'DOB', 'POB', 'DOD', 'POD', 'Link']  # Replace with actual column names

# Read the TSV file into a DataFrame
df = pd.read_csv(file_path, sep='\t', header=None, names=columns)

# Print the DataFrame
print(df)
