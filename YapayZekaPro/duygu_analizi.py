from textblob import TextBlob
from vaderSentiment.vaderSentiment import  SentimentIntensityAnalyzer


def analyze_sentiment_textblob(text):
    sentiment = TextBlob(text).sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment <0:
        return "Negative"
    else:
        return "Neutral"
"""
text = "Python programalamyı seviyorum"
print(f"Sentiment {analyze_sentiment_textblob(text)}")
"""
analyzer = SentimentIntensityAnalyzer()
def analyze_sentiment_vader(text):
    sentiment_score = analyzer.polarity_scores(text)["compound"]
    if sentiment_score >=0.05:
        return "Positive"
    elif sentiment_score <=-0.05:
        return "Negative"
    else:
        return "Neutral"

def analyze_user_input():
    while True:
        text = input("lütfen metni giriniz (exit)")
        if text.lower() == 'exit':
            print("Çıkış yapılıyor")
            break
        else:
            print(f"TextBlob Sentiment : {analyze_sentiment_textblob(text)}")
            print(f"Vader Sentiment: {analyze_sentiment_vader(text)}")
analyze_user_input()