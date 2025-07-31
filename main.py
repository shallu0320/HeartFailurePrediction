import pandas as pd

# Load the CSV file
df = pd.read_csv("heart.csv")

# Show the first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Show basic statistics
print("\nBasic Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())


import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv("heart.csv")  # Make sure this file exists in your folder

# Example plot: Age vs MaxHR
plt.figure(figsize=(10, 6))
plt.scatter(df["Age"], df["MaxHR"], alpha=0.6, c='red', edgecolors='k')
plt.title("Age vs Maximum Heart Rate")
plt.xlabel("Age")
plt.ylabel("Max Heart Rate")
plt.grid(True)

# Show the plot
plt.show()
