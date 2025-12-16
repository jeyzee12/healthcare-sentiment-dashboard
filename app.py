import streamlit as st
import pandas as pd

st.set_page_config(page_title="Healthcare Sentiment Dashboard", layout="wide")

# Load data
df = pd.read_csv("healthcare_twitter_sentiment.csv")
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Title
st.title("Social Media Sentiment Analysis on Healthcare Services")
st.write("This dashboard visualizes public sentiment toward hospital and healthcare services using Twitter data.")

# Sidebar filters
st.sidebar.header("Filters")

sentiment_filter = st.sidebar.multiselect(
    "Select Sentiment",
    options=df["sentiment"].unique(),
    default=df["sentiment"].unique()
)

df_filtered = df[df["sentiment"].isin(sentiment_filter)]

# Visualizations
st.subheader("Sentiment Distribution")
st.bar_chart(df_filtered["sentiment"].value_counts())

st.subheader("Sentiment Trends Over Time")
sentiment_time = (
    df_filtered
    .groupby([df_filtered["date"].dt.to_period("M"), "sentiment"])
    .size()
    .unstack()
    .fillna(0)
)
st.line_chart(sentiment_time)

st.subheader("Sample Tweets")
st.dataframe(df_filtered[["tweet_text", "sentiment"]].head(20))

# Footer
st.markdown("---")
st.markdown("**Data Source:** Kaggle – Sentiment140 Twitter Dataset")
