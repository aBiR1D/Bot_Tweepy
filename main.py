import tweepy 

client = tweepy.Client(consumer_key="API_KEY",
                    consumer_secret="API_KEY_SECRET",
                    access_token="ACCESS_TOKEN",
                    access_token_secret="ACCESS_TOKEN_SECRET")

response = client.create_tweet(text='hello world from api, test 1')