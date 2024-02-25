from twitterAPI import twitterAPI
from tweet import tweet
import pandas as pd
import time
import os

# connect to database and collect tweets
test = twitterAPI(os.environ['postgres_user'], os.environ['postgres_password'], 'twitterDB')
tweet_df = pd.read_csv(r'C:\Users\annik\OneDrive\Documents\Downloads\hw1_data\tweet.csv')

# post tweets
start_time = time.time()
for index, row in tweet_df.iterrows():
    new_tweet = tweet(row['USER_ID'], row['TWEET_TEXT'])
    test.post_tweet(new_tweet)
end_time = time.time()

# calculate tweets per second
twts_per_sec = len(tweet_df) / (end_time - start_time)
print("Tweets posted per second:", twts_per_sec)