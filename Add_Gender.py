import pandas as pd

# Define the file path
file_path = 'C:/CCLAMP_gender/C-CLAMP_metadata.txt'

# Define the column names
columns = ['File', 'Year', 'Title', 'Author', 'DOB', 'POB', 'DOD', 'POD', 'Link']  # Add column names

# Read the txt file into a DataFrame
df = pd.read_csv(file_path, sep='\t', header=None, names=columns)


# Define a function to determine gender based on the 'Author' column
def determine_gender(author):
    if author == 'NA':
        return 'NA'
    elif ';' in author:
        return 'Mixed'
    else:
        return 'X'


# Apply the function to create the 'Gender' column
df['Gender'] = df['Author'].apply(determine_gender)

# Print the DataFrame
print(df)
