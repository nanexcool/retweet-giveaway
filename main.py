from decouple import config
import tweepy

auth = tweepy.OAuthHandler(config('CONSUMER_KEY'), config('CONSUMER_SECRET'))
auth.set_access_token(config('ACCESS_TOKEN'), config('ACCESS_TOKEN_SECRET'))

api = tweepy.API(auth)

# my tweet
id = '1381347584934051846'

# get up to 100 retweeters (more is hard)
retweets_list = api.retweets(id, 100)

for retweet in retweets_list:
    print(retweet.user.screen_name)
