# eda.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('data/heart.csv')  # Adjust path if needed

# Example EDA plot
sns.countplot(x='HeartDisease', data=df)
plt.title('Heart Disease Count')
plt.show()
