import pandas as pd

# Load the scraped dataset
df = pd.read_csv("books.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nAverage price by category:")
category_avg = df.groupby("category")["price"].mean()
print(category_avg)

df.to_csv("cleaned_books.csv", index=False)

print("\nCleaned dataset saved as cleaned_books.csv")
