import pandas as pd

# Load the first dataset
df1 = pd.read_csv('diabetes_dataset.csv')  # Replace 'Dataset1.csv' with your actual file path

# Load the second dataset
df2 = pd.read_csv('augmented_diabetes_dataset.csv')  # Replace 'Dataset2.csv' with your actual file path

# Concatenate the datasets vertically
combined_df = pd.concat([df1, df2], ignore_index=True)

# Save the combined dataset to a new CSV file
combined_df.to_csv('combined_diabetes_dataset.csv', index=False)

print("Combined dataset saved as 'combined_diabetes_dataset.csv'")
