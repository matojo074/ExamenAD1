import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

###API ########################
consumer_key = 
consumer_secret = 
access_token = 
access_token_secret = 

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
    db = server.create('jolimpicos')
except:
    db = server['jolimpicos']

'''===============LOCATIONS=============='''

twitterStream.filter(locations=[-83.6,-56.2,-34.3,14.9])
twitterStream.filter(track=['JuegosOlimpios'])
