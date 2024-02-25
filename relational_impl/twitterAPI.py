from utils import utils
from datetime import datetime
from tweet import tweet

class twitterAPI:
    tweet_id = 0

    def __init__(self, user, password, database, host="localhost"):
        self.dbu = utils(user, password, database, host)

    def post_tweet(self, twt):
        """ posts a single tweet to db """
        now = datetime.now()
        tweet_ts = now.strftime("%Y-%m-%d %H:%M:%S")

        twitterAPI.tweet_id += 1

        sql = "INSERT INTO tweet (tweet_id, user_id, tweet_ts, tweet_text) VALUES (%s, %s, %s, %s) "
        val = (twitterAPI.tweet_id, twt.user_id, tweet_ts, twt.tweet_text)
        self.dbu.insert_one(sql, val)

    def get_users(self):
        """ return a list of all user ids"""
        sql = "SELECT user_id FROM follows"
        df = self.dbu.execute(sql)
        return df.iloc[:, 0].tolist()

    def get_followers(self, userid):
        """ gets the followers of the randomly selected user """
        sql = f"SELECT follows_id FROM follows WHERE user_id = {userid}"
        df = self.dbu.execute(sql)
        return df.iloc[:, 0].tolist()

    def home_timeline(self, userid):
        """ gets the 10 most recent tweets from the user's followers """
        sql = f"SELECT t.user_id, t.tweet_text FROM tweet t " \
              f"JOIN follows f ON t.user_id = f.follows_id " \
              f"WHERE f.user_id = {userid} " \
              f"ORDER BY t.tweet_ts DESC LIMIT 10"
        df = self.dbu.execute(sql)
        twts = [tweet(*df.iloc[i][:]) for i in range(len(df))]
        return twts


