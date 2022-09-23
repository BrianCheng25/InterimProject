#import sntwitter for get tweets
import snscrape.modules.twitter as sntwitter
#import pandasd for making a dataframe
import pandas as pd

# query format and limit
query = " #Coronavirus until:2019-03-31 since:2019-01-01" # search by keywords
#query = "(from:eafifaesports) until:2019-09-01 since:2018-09-01" # search by user
tweets = [] # tweets (var) = list 
limit = 1000 # tweets limit i wanna get

# To get tweet by using sntwitter
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
      #print(vars(tweet)) # Raw data from tweets
      #break 
    if len(tweets) == limit: # Get tweet till it reached the limit set above
        break # Condition = True jau end loop
    else: # Get all tweet and put into a list 
        tweets.append([tweet.date, tweet.username, tweet.content])
        
# Make the list into a dataframe by using pandas
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)

# to save to csv
df.to_csv('20190103tweets.csv')