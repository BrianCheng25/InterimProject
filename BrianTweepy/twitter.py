import tweepy
import pandas as pd
#填寫twitter提供的開發Key和secret
api_key = 'ietuiQAMZ5E0hUvGnJ2txlzuj'
api_key_secret = 'z09Oif7SCYcFSUvPrxtUQclHlNbZMPvw8pnccb9qLyaxcrApf5'
access_token = '1571506386051399680-EI2R3E8G3DVHWkBbmhPMyjg4qtLrYK'
access_token_secret = '2axVtmZuwpO1sKxNmOd2JLKrYAM6oi6p60OFnSdM8HZsd'
#提交你的Key和secret
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
#獲取類似於內容控制代碼的東西
api = tweepy.API(auth)
from tweepy import OAuthHandler
from tweepy import API
# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# user tweets
user = 'JoeBiden'
limit=300

tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode='extended').items(limit)

# search tweets
# keywords = 'apple'
# limit = 50

# tweets = tweepy.Cursor(api.search_tweets, q=keywords, count=100, tweet_mode='extended').items(limit)

# tweets = api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')

# create DataFrame
columns = ['User', 'Tweet']
data = []

for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text])

df = pd.DataFrame(data, columns=columns)

print(df)
