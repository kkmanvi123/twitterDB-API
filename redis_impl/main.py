from redisAPI import redisAPI
import csv
import time
import random as rnd
from tweet import tweet

# files to include
tweet_file = 'tweet.csv'
follows_file = 'follows.csv'

# initialize API
api = redisAPI()
api.loadFollows(follows_file)

# open tweet file, read and post each tweet
start_time = time.time()
with open(tweet_file, 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        new_tweet = tweet(row[0], row[1])
        api.postTweet(new_tweet)
end_time = time.time()

# calculate tweets per second
twts_per_sec = 1000000 / (end_time - start_time)
print("Tweets posted per second:", twts_per_sec)

# calculate timelines per second
n = 100
start_time = time.time()
for i in range(n):
    api.getTimeline(rnd.randrange(1, 9999))
end_time = time.time()

timelines_per_sec = n / (end_time - start_time)
print('Timelines retrieved per second:', timelines_per_sec)