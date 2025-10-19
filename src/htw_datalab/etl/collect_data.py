import os
import tweepy
import time
import pandas as pd
    
def get_tweets_and_save(bearer_token: str, company_tweet: str) -> None:
    # ========================
    # 1. Authenticate
    # ========================
    client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)

    # ========================
    # 2. Get User ID for @TLRailUK
    # ========================
    user = client.get_user(username=company_tweet)
    user_id = user.data.id
    print(f"TLRailUK user ID: {user_id}")

    # ===============================
    # 3. Retrieve Latest 100 Tweets
    # ===============================
    tweets_data = []

    for response in tweepy.Paginator(
        client.get_users_tweets,
        id=user_id,
        tweet_fields=["created_at", "public_metrics", "text"],
        max_results=100  # max per request
    ).flatten(limit=100):  # limit total number
        tweets_data.append({
            "created_at": response.created_at,
            "text": response.text,
            "retweets": response.public_metrics.get("retweet_count", 0),
            "likes": response.public_metrics.get("like_count", 0),
            "replies": response.public_metrics.get("reply_count", 0),
            "quotes": response.public_metrics.get("quote_count", 0)
        })

    # ===============================
    # 4. Save to CSV
    # ===============================
    df = pd.DataFrame(tweets_data)
    df.to_csv("./TLRailUK_latest_100_tweets.csv", index=False)

    print(f"✅ Retrieved {len(df)} tweets and saved to TLRailUK_latest_100_tweets.csv")
