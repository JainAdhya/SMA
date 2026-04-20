import pandas as pd
import numpy as np
import re

# Load data
df = pd.read_excel("uncleaned_regional.xlsx")

# Display initial data
print("Original Data:")
print(df.head())

# ----------------------------
# 1. Handle missing values
# ----------------------------
df['Likes'] = df['Likes'].replace('—', np.nan)
df['Likes'] = pd.to_numeric(df['Likes'])

# Fill missing likes with median
df['Likes'] = df['Likes'].fillna(df['Likes'].median())

# ----------------------------
# 2. Clean text function
# ----------------------------
def clean_text(text):
    if pd.isnull(text):
        return text
    
    # Remove extra spaces
    text = str(text).strip()
    text = re.sub(r'\s+', ' ', text)
    
    # Optional: remove emojis (basic range cleanup)
    text = re.sub(r'[^\w\s\u0900-\u097F\u0980-\u09FF!?.]', '', text)
    
    return text

# Apply cleaning on Comment column
df['Comment'] = df['Comment'].apply(clean_text)

# ----------------------------
# 3. Standardize Language column
# ----------------------------
df['Language'] = df['Language'].str.lower().str.strip()

# ----------------------------
# 4. Remove duplicates
# ----------------------------
df = df.drop_duplicates()

# ----------------------------
# 5. Reset index
# ----------------------------
df = df.reset_index(drop=True)

# ----------------------------
# 6. Final cleaned data
# ----------------------------
print("\nCleaned Data:")
print(df)

# Save cleaned file
df.to_excel("cleaned_regional.xlsx", index=False)

print("\nCleaned file saved as 'cleaned_regional.xlsx'")