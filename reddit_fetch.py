import requests

url = "https://releasetrain.io/api/reddit"

try:
    response = requests.get(url)
    response.raise_for_status()  
    reddit_data = response.json()

    print(f"✅ Fetched {len(reddit_data)} Reddit posts.\n")
    
    for post in reddit_data[:5]:
        print("Title:", post['title'])
        print("Author:", post.get('author', 'N/A'))
        print("-" * 50)

except requests.exceptions.RequestException as e:
    print("❌ Failed to fetch data from API.")
    print(e)
from textblob import TextBlob

print("\n🧠 Sentiment Analysis on Top 10 Titles:\n")

for i, post in enumerate(reddit_data[:10]):
    title = post['title']
    sentiment_score = TextBlob(title).sentiment.polarity

    if sentiment_score > 0.1:
        label = "Positive"
    elif sentiment_score < -0.1:
        label = "Negative"
    else:
        label = "Neutral"

    print(f"{i+1}. {title}")
    print(f"   Sentiment: {label} (Score: {sentiment_score:.2f})\n")