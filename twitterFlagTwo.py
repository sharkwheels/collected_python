import requests, serial, re
from twython import Twython
from twython import TwythonStreamer

### GET KEYS (LOCAL) ######################################

keys = []
with open('twitter.txt','r') as my_file:
    keys = my_file.read().splitlines()

TWIT_KEY = keys[0]
TWIT_SECRET = keys[1]
OAUTH_TOKEN = keys[2]
OAUTH_TOKEN_SECRET = keys[3]

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
twitter.verify_credentials()

ser = serial.Serial('/tmp/tty.LightBlue-Bean', 9600, timeout=0.25)

# this is just pulled right off the twython docs: https://twython.readthedocs.org/en/latest/usage/streaming_api.html
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:

            bodyOf = data['text'].encode('utf-8')
            command = "hello"
            acct = '@SydneyTheCat'

            print data['user']['screen_name'].encode('utf-8')
            
            if bodyOf.startswith(acct) and command in bodyOf:
                bodyStrip = re.sub(r'[^\w\s]','',bodyOf.lower())
                ser.write("T")
            elif bodyOf.startswith(acct) and command not in bodyOf:
                print 'sorry no command'
            else:
                print "neither thing was found"


    def on_error(self, status_code, data):
        print status_code

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()

stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
stream.statuses.filter(track='@SydneyTheCat') 