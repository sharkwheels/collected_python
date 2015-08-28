import requests, serial 
from twython import Twython
from twython import TwythonStreamer

# you might want to shove this in a config file. I'm lazy. 

APP_KEY = ""
APP_SECRET = ""

# Access Tokens

OAUTH_TOKEN = ""
OAUTH_TOKEN_SECRET = ""

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
twitter.verify_credentials()

ser = serial.Serial('/tmp/tty.LightBlue-Bean', 9600, timeout=0.25)

# this is just pulled right off the twython docs: https://twython.readthedocs.org/en/latest/usage/streaming_api.html
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')
            print data['user']['screen_name'].encode('utf-8')
            ser.write("T")

    def on_error(self, status_code, data):
        print status_code

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()

stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

stream.statuses.filter(track='@_nadine') #kinda hacky, but it works. This is filtering the public stream and just looking for '@_nadine', it can look for anything. 