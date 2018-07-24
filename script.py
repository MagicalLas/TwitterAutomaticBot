import tweepy
consumerKey = "drUtc6UoLs5gPM3UOclKzkGkK"
consumerSecret = "uup8NH3yClVDSsyB8QhAyoxcpkECF5FoKaaa6AaZ5EkeZqX3KF"
IKATTHAN_T = '991093379852259328-YbbXKR36iDZ4cPTl0sQSx7VCVzH4Mxv'
IKATTHAN_S = 'PHUD6ha7Pz1QsQGluFllH9ZV9xFzZMp2hybVs3BrV7wSU'
'''
auth  =  tweepy . OAuthHandler ( consumerKey ,  consumerSecret )
#auth.get_authorization_url()
accessToken = IKATTHAN_T
accessTokenSecret = IKATTHAN_S
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)
'''
class Twitter:
    def __init__(self):
        consumerKey = "drUtc6UoLs5gPM3UOclKzkGkK"
        consumerSecret = "uup8NH3yClVDSsyB8QhAyoxcpkECF5FoKaaa6AaZ5EkeZqX3KF"
    def auth(self, IT, IS):
        self.auth  =  tweepy . OAuthHandler (consumer_key, consumer_secret)
        self.auth.set_access_token(IT, IS)
        self.api = tweepy.API(auth)
    def newAccount(self):
        return self.auth.get_authorization_url()
    def joinAccount(self, pin):
        self.auth.
    def tweet(self,string):
        self.api.update_status(status=string)
tw = Twitter()
tw.auth(IKATTHAN_T, IKATTHAN_S)

while(True):
    _tweet = input('>')
    tw.tweet(_tweet)
    