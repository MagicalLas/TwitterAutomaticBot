import tweepy
consumerKey = "drUtc6UoLs5gPM3UOclKzkGkK"
consumerSecret = "uup8NH3yClVDSsyB8QhAyoxcpkECF5FoKaaa6AaZ5EkeZqX3KF"
auth  =  tweepy . OAuthHandler ( consumerKey ,  consumerSecret )
#auth.get_authorization_url()
IKATTHAN_T = '991093379852259328-YbbXKR36iDZ4cPTl0sQSx7VCVzH4Mxv'
IKATTHAN_S = 'PHUD6ha7Pz1QsQGluFllH9ZV9xFzZMp2hybVs3BrV7wSU'
accessToken = IKATTHAN_T
accessTokenSecret = IKATTHAN_S
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

while(True):
    tweet = input('>')
    api.update_status(status=tweet)