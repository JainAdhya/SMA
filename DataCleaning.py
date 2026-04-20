import pandas as pd
import numpy as np

# Load dataset (replace with your file if needed)
df = pd.read_csv("uncleaned.csv")

# 1. Remove unwanted column
df = df.drop(columns=["Unnamed: 0"], errors='ignore')

# 2. Strip extra spaces from all string columns
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# 3. Standardize Sentiment column
df['Sentiment'] = df['Sentiment'].str.capitalize()

# 4. Handle missing values

# Fill missing text with placeholder
df['Text'] = df['Text'].fillna("No Comment")

# Fill missing sentiment with Neutral
df['Sentiment'] = df['Sentiment'].fillna("Neutral")

# Fill missing categorical values
df['User'] = df['User'].fillna("Unknown")
df['Platform'] = df['Platform'].fillna("Unknown")
df['Country'] = df['Country'].fillna("Unknown")

# Fill missing Likes with 0 and convert to int
df['Likes'] = pd.to_numeric(df['Likes'], errors='coerce').fillna(0).astype(int)

# 5. Remove rows where Text is empty after cleaning
df = df[df['Text'].str.strip() != ""]

# 6. Remove duplicate rows
df = df.drop_duplicates()

# 7. Reset index
df = df.reset_index(drop=True)

# 8. Save cleaned dataset
df.to_csv("cleaned.csv", index=False)

# 9. Display cleaned data
print(df)