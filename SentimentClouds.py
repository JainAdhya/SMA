import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load dataset
df = pd.read_csv("sentimentdataset.csv")

# Clean column names & values
df.columns = df.columns.str.strip()
df['Sentiment'] = df['Sentiment'].str.strip()

# Take top 20 rows (optional but good for exam)
df = df.head(20)

# -----------------------------
# Create function for word cloud
# -----------------------------
def create_wordcloud(text, title):
    wc = WordCloud(width=800, height=400, background_color='white')
    wc.generate(text)

    plt.figure()
    plt.imshow(wc)
    plt.axis("off")
    plt.title(title)
    plt.show()

# -----------------------------
# Separate text by sentiment
# -----------------------------
positive_text = " ".join(df[df['Sentiment'] == 'Positive']['Text'])
negative_text = " ".join(df[df['Sentiment'] == 'Negative']['Text'])
neutral_text  = " ".join(df[df['Sentiment'] == 'Neutral']['Text'])

# -----------------------------
# Generate Word Clouds
# -----------------------------
create_wordcloud(positive_text, "Positive Sentiment Cloud")
create_wordcloud(negative_text, "Negative Sentiment Cloud")
create_wordcloud(neutral_text,  "Neutral Sentiment Cloud")