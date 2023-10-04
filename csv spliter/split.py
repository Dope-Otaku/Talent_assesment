import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('qw.csv')

# Split the options in the cell based on ","
df['Options'] = df['Options'].str.split(',')

# Create four new columns and assign the options to them
df['Option 1'] = df['Options'].str[0]
df['Option 2'] = df['Options'].str[1]
df['Option 3'] = df['Options'].str[2]
df['Option 4'] = df['Options'].str[3]

# Drop the original 'Options' column
df.drop('Options', axis=1, inplace=True)

# Save the modified DataFrame back to a CSV file
df.to_csv('updated_file.csv', index=False)
