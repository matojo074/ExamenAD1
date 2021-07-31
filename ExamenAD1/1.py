import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

###API ########################
consumer_key = "irnK8KT1RrNyV9OUQDHwQ5Icx"
consumer_secret = "IuMMfp8DM5uFjOJlu5iceDnqkzK2CkS7PkBTbTBRNR7Upgq5mP"
access_token = "784853519497105408-8OXTILd2D1ppzvQf1jO9LY8L8iuyyZc"
access_token_secret = "vpsfDZIzs7JcQbLo27odaSxST3MbQEsDvypkwqvlduiKd"

#####################################
class listener(StreamListener):

    def on_data(self, data):
        dictTweet = json.loads(data)
        try:

            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print("SAVED" + str(doc) + "=>" + str(data))
        except:
            print("Already exists")
            pass
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://admin:FARAaM12@127.0.0.1:5984')
try:
    db = server.create('jolimpicosgermany')
except:
    db = server['jolimpicosgermany']

'''===============LOCATIONS=============='''

twitterStream.filter(locations=[4.95,47.18,16.01,54.45])
# [-99.7245,18.93,-98.5167,19.9627],[126.643,37.3116,127.3154,37.8219]