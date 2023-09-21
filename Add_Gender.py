import pandas as pd
from gender_from_name.detector import get_gender

# Define the file path
file_path = 'C:/CCLAMP_gender/C-CLAMP_metadata.txt'

# Define the column names
columns = ['File', 'Year', 'Title', 'Author', 'DOB', 'POB', 'DOD', 'POD', 'Link']  # Add column names

# Read the txt file into a DataFrame
df = pd.read_csv(file_path, sep='\t', header=None, names=columns)


# Define a function to determine gender based on the 'Author' column
def determine_gender(author):
    if pd.notna(author):
        if ';' in author:
            print(author + ": mixed")
            return 'mixed'
        else:
            first_name = author.split()[0]
            gender = get_gender(first_name)
            if gender is not None:
                print(author + ", " + first_name + ": " + gender)
                return gender
    else:
        return 'NA'


# Apply the function to create the 'Gender' column
df['Gender'] = df['Author'].apply(determine_gender)

# Define the file path for the output CSV file
output_file_path = 'C:/CCLAMP_gender/C-CLAMP_metadata_gender.csv'

# Write the DataFrame to a CSV file
df.to_csv(output_file_path, index=False)