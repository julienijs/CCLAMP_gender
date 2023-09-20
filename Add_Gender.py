import pandas as pd

# Define the file path
file_path = 'your_file.txt'

# Define the column names
columns = ['Column1', 'Column2', 'Column3']  # Replace with actual column names

# Read the TSV file into a DataFrame
df = pd.read_csv(file_path, sep='\t', header=None, names=columns)

# Print the DataFrame
print(df)
