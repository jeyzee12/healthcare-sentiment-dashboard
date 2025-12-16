import pandas as pd

df = pd.read_csv(
    "training.1600000.processed.noemoticon.csv",
    encoding="latin-1",
    header=None
)

df.columns = ["sentiment", "tweet_id", "date", "query", "user", "tweet_text"]

df["sentiment"] = df["sentiment"].map({0: "Negative", 4: "Positive"})

keywords = [
    "hospital", "doctor", "nurse", "clinic",
    "healthcare", "medical", "covid", "er", "icu"
]

health_df = df[df["tweet_text"].str.contains("|".join(keywords), case=False, na=False)]

health_df = health_df[["tweet_text", "sentiment", "date"]]
health_df["topic"] = "Healthcare Services"
health_df["source"] = "Twitter"

health_df = health_df.head(500)

health_df.to_csv("healthcare_twitter_sentiment.csv", index=False)

print("Healthcare dataset created successfully!")
