import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (convert your data into CSV first)
df = pd.read_csv("sentimentdataset.csv")

# Clean column names
df.columns = df.columns.str.strip()
df = df.head(20)
# -----------------------------
# 1. Sentiment Count (Bar Chart)
# -----------------------------
sentiment_count = df['Sentiment'].value_counts()

plt.figure()
sentiment_count.plot(kind='bar')
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()

# -----------------------------
# 2. Platform Usage (Pie Chart)
# -----------------------------
platform_count = df['Platform'].value_counts()

plt.figure()
platform_count.plot(kind='pie', autopct='%1.1f%%')
plt.title("Platform Distribution")
plt.ylabel("")
plt.show()

# -----------------------------
# 3. Likes vs Retweets (Scatter)
# -----------------------------
plt.figure()
plt.scatter(df['Likes'], df['Retweets'])
plt.title("Likes vs Retweets")
plt.xlabel("Likes")
plt.ylabel("Retweets")
plt.show()

# -----------------------------
# 4. Posts per Country (Bar)
# -----------------------------
country_count = df['Country'].value_counts()

plt.figure()
country_count.plot(kind='bar')
plt.title("Posts by Country")
plt.xlabel("Country")
plt.ylabel("Count")
plt.show()