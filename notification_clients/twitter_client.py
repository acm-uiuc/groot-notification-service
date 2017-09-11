import tweepy


class TwitterClient:
    def __init__(self,
                 consumer_key=None,
                 consumer_secret=None,
                 access_key=None,
                 access_secret=None):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        self.client = tweepy.API(auth)

    def send(self, message):
        self.client.update_status(message)
