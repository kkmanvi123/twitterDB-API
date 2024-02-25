class tweet:
    def __init__(self, user_id, tweet_text):
        self.user_id = user_id
        self.tweet_text = tweet_text

    def __str__(self):
        return f'Tweet(User: {self.user_id}, Text: {self.tweet_text})'
