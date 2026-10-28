# Read the csv file
import pandas as pd
from pathlib import Path

data_path = Path("data/Bitext_Sample_Customer_Support_Training_Dataset_27K_responses-v11.csv")

df = pd.read_csv(data_path)

print("Dataset loaded successfully!")
print(f"Number of rows: {len(df)}")
print(f"Number of columns: {len(df.columns)}")
print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())
