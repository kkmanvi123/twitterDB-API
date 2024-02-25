import csv
import redis
from datetime import datetime


class redisAPI:

    def __init__(self):
        """ initialize API """
        self.tweet_id = 0
        self.r = redis.Redis('localhost', 6379, decode_responses=True)
        self.r.flushall()

   def postTweet(self, twt):
       """ takes a tweet object and posts it """
       self.tweet_id += 1
       if self.tweet_id % 10000 == 0:
           print("Posted tweet", self.tweet_id)

       tweet_info = {
           'user_id': twt.user_id,
           'tweet_text': twt.tweet_text,
           'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
       }

       self.r.hmset(f'tweet_id:{self.tweet_id}', tweet_info)
       self.updateTimelines(self.r.smembers(f'followers:{twt.user_id}'), self.tweet_id)

   def loadFollows(self, csv_file):
       """ load csv file containing follower information """
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                user_id, follows_id = row
                self.r.sadd(f'followers:{follows_id}', user_id)

    def updateTimelines(self, followers, tweet_id):
        """ updates timelines of followers once a tweet is posted """
        for user in followers:
            self.r.lpush(f'timeline:{user}', self.r.hget(f'tweet_id:{tweet_id}', 'tweet_text'))

    def getTimeline(self, user_id):
        """ retrieves timeline of a specific user """
        try:
            return self.r.lrange(f'timeline:{user_id}', 0, 9)
        except redis.exceptions.ResponseError:
            return list()