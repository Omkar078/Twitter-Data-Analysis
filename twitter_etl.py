import tweepy
import pandas as pd
import json
import datetime as datetime
import s3fs

access_key = "YlpKT6n7v0S8Sw1B7a8lV6Cbp"
access_secret = "hjY35iwqbhVlGQpVKC21kYXbysYD96UkecexNqavUuZPkgihfB"
consumer_key =  "1544034567614451713-V4HvBmJpP9AYQhTQeTFoplp21yZ9IK"
consumer_secret = "GYb4qvcJfQDrMPjvOL6atX7raWyKq9e5UR9A6TRmozUDf"


#twitter aunthentication
auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key, consumer_secret)

# creating an API object
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name = '@elonmusk',
                            # 200 is the maximum allowed count
                            count = 200,
                            include_rts = False,
                            # Necessary to keep full_text
                            # otherwisie onlyb the first 140 words are extended
                            tweet_mode = 'extended'
                            )

print(tweets)