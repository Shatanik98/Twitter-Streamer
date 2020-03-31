# Variables that contain user credentials to access Twitter API.
access_token = "2431996178-1pJ11yGH6xVFrRiWRsWn614riUfQEbQEy7sCPNb"
access_token_secret = "ZjI6sJbZU3iZrKrlB2AeiTfYSGASrwFqeIemkrTQlhs2I"
consumer_key = "QNTCcNbdR8UWISZdLsmTdXHEy"
consumer_secret = "4vcdQ9SXGHjLbxYKXAXSbAmtqyY0uHRYXbushqAEmkwSEgv98F"

# Streaming
# StreamListener is a class of the tweepy.streaming module.
# OAuthHandler is a class that handles authentication associated with the Twitter app.
from tweepy.streaming import StreamListener 
from tweepy import Stream
from tweepy import OAuthHandler

# The StdOutListener class inherits from the StreamListener class.
class StdOutListener(StreamListener):
    # Two methods are required, viz. on_data and on_error.
    # on_data method is used to retrieve data from the stream.
    # on_error is used to retrieve errors in the stream.
    def on_data(self, data):
        print(data)
        return True
    
    def on_error(self, status):
        print(status)

# Main section of the program.
if __name__ == "__main__":
    
    listener = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listener)

    # To copy the contents of the bag of words file to a list.
    var = open("Keywords_Final.txt", "rt")
    list1 = var.readlines()
    list2 = [x.replace("\n", " ") for x in list1]
    
    # Using the list of keywords to filter twitter data.
    stream.filter(track = list2)