def create_cloud(text, title, font):
    wc = WordCloud(
        width=800,
        height=400,
        background_color='white',
        font_path=font
    )
    
    wc.generate(text)

    import matplotlib.pyplot as plt
    plt.figure()
    plt.imshow(wc)
    plt.axis("off")
    plt.title(title)
    plt.show()

# Separate by language + sentiment
eng_pos = " ".join(df[(df['Language']=='english') & (df['Sentiment']=='Positive')]['Comment'])
hin_pos = " ".join(df[(df['Language']=='hindi') & (df['Sentiment']=='Positive')]['Comment'])
ben_pos = " ".join(df[(df['Language']=='bengali') & (df['Sentiment']=='Positive')]['Comment'])

# Generate clouds
create_cloud(eng_pos, "English Positive", "arial.ttf")
create_cloud(hin_pos, "Hindi Positive", r"NotoSansDevanagari-Regular.ttf")
create_cloud(ben_pos, "Bengali Positive", r"NotoSansBengali-Regular.ttf")