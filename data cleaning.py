import pandas as pd

# Load dataset
file_path = "dataset.csv"  # Update with actual file path
df = pd.read_csv(file_path, header=None)

# Rename columns
df.columns = ['user_id', 'game_title', 'action', 'value', 'unknown_column']

# Drop unnecessary column
df = df.drop(columns=['unknown_column'])

# Handle missing values (if any)
df = df.dropna()

# Convert data type
df['user_id'] = df['user_id'].astype(int)
df['game_title'] = df['game_title'].astype(str)
df['action'] = df['action'].astype(str)
df['value'] = df['value'].astype(float)

# Remove duplicate entries
df = df.drop_duplicates()

# Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)

print("Data cleaning completed. Cleaned dataset saved as 'cleaned_dataset.csv'.")
