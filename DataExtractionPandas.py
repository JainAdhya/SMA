import csv
import pandas as pd

# Step 1: Load dataset using pandas
df = pd.read_csv('sentimentdataset.csv', encoding='utf-8')

# Step 2: Display first 5 rows
print("First 5 Rows of Dataset:")
print(df.head())

# Step 3: Extract column names
print("\nColumn Names:")
print(df.columns.tolist())

# Step 4: Extract specific columns
print("\nExtracted Data (Text & Sentiment):")
print(df[['Text', 'Sentiment']].head())

# Step 5: Extract rows with Positive sentiment
positive_data = df[df['Sentiment'].str.strip() == 'Positive']

print("\nPositive Sentiment Data:")
print(positive_data[['User', 'Text']].head())

# Step 6: Save extracted data into new CSV
positive_data.to_csv('positive_data.csv', index=False)

print("\nData extraction completed and saved successfully!")