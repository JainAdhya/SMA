import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os

# 1. Dataset with distinct Positive and Negative Hindi comments
data = {
    'Comment': ['बहुत अच्छा', 'बेहतरीन क्वालिटी', 'शानदार', 
                'बहुत खराब', 'बर्बाद', 'घटिया सर्विस',
                'शानदार अनुभव', 'अच्छा है', 'बेकार'],
    'Sentiment': ['Positive', 'Positive', 'Positive', 
                  'Negative', 'Negative', 'Negative', 
                  'Positive', 'Positive', 'Negative']
}
df = pd.DataFrame(data)

# 2. Correct Hindi Font Path (FIXED)
font_p = r"C:\Windows\Fonts\Nirmala.ttc"

# 3. Function to generate and show/save word cloud
def generate_regional_cloud(sentiment_type, title, color_map, save_name):
    
    # Filter text
    text = " ".join(df[df['Sentiment'] == sentiment_type]['Comment'])
    
    if not text.strip():
        print(f"No data for {sentiment_type}")
        return
    
    # Create WordCloud (Hindi-safe)
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        font_path=font_p,
        regexp=r"[\u0900-\u097F]+",  # Keeps Hindi words intact
        colormap=color_map
    ).generate(text)
    
    # Plot
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud)
    plt.title(title, fontsize=14)
    plt.axis("off")
    
    # Save image
    wordcloud.to_file(save_name)
    print(f"Saved: {save_name}")
    
    plt.show()

# 4. Generate both clouds
generate_regional_cloud('Positive', 'Hindi Positive Word Cloud', 'Greens', 'positive_hindi.png')
generate_regional_cloud('Negative', 'Hindi Negative Word Cloud', 'Reds', 'negative_hindi.png')