import tweepy
from time import sleep
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

    def Auth(self, IT, IS):
        self.auth = tweepy . OAuthHandler(
            consumerKey, consumerSecret)
        self.auth.set_access_token(IT, IS)
        self.api = tweepy.API(self.auth)
        return

    def newAccount(self):
        return self.auth.get_authorization_url()

    def joinAccount(self, pin):
        self.auth.pin = pin

    def tweet(self, string):
        self.api.update_status(status=string)


tw = Twitter()
tw.Auth(IKATTHAN_T, IKATTHAN_S)
count = 14
while(True):
    _tweet = input('>')+'\r\n'+"#아유님이_보고싶어 #보고싶을떄_올라오는_자동트윗 "+"\r\n벌써"+str(count)+"번째..."
    count+=1
    try:
        tw.tweet(_tweet)
    except:
        try:
            tw.tweet("너무 자주보고싶어합니다.")
        except:
            pass
        print("너무 자주보고싶어합니다.")
        sleep(5)

    
