import tweepy


class Twitter:
    def __init__(self):
        consumerKey = "drUtc6UoLs5gPM3UOclKzkGkK"
        consumerSecret = "uup8NH3yClVDSsyB8QhAyoxcpkECF5FoKaaa6AaZ5EkeZqX3KF"
        self.auth = tweepy.OAuthHandler(
            consumerKey, consumerSecret)

    def Auth(self, IT, IS):
        self.auth.set_access_token(IT, IS)
        self.api = tweepy.API(self.auth)
        return
    
    def _auth(self):
        return self.auth

    def newAccount(self):
        return self.auth.get_authorization_url()

    def joinAccount(self, verifier):
        a, b = self.auth.get_access_token(verifier)
        self.auth.set_access_token(
            a, b)

    def tweet(self, string):
        self.api.update_status(status=string)



f = open("./tweet.html", 'r')
lines = f.readlines()
tweet_html = ""
for i in lines:
    tweet_html += i
tweet_html += ""

from sanic import Sanic, response
from sanic.response import text, html
import datetime

app = Sanic()
tw = Twitter()


@app.route("/message")
async def index(request):
    return response.redirect(tw.newAccount())


@app.route("/")
async def send_message(request):
    try:
        verifier = request.args['oauth_verifier'][0]
    except Exception:
        return text("Missing Data")

    response = html(tweet_html)
    response.cookies['verif'] = verifier
    auth = tw._auth()
    a,b = auth.get_access_token(verifier)
    response.cookies['a'] = a
    response.cookies['b'] = b
    return response

@app.route("/tweet")
async def tweet(request):
    try:
        a = request.cookies.get('a')
        b = request.cookies.get('b')
        message = request.args['m'][0]
        hash = request.args['h'][0]
    except Exception:
        print(request.args)
        return text("Missing Data")

    response = text('0')
    auth = tw._auth()
    auth.set_access_token(a,b)
    api = tweepy.API(auth)
    api.update_status(message + "\n" + hash)
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
