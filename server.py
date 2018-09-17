import sys
import codecs
sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

import requests
from requests import request
import requests_oauthlib

import tweepy
from flask import Flask, redirect, url_for, session


app = Flask(__name__)

consumer_key = 'drUtc6UoLs5gPM3UOclKzkGkK'
consumer_secret = 'uup8NH3yClVDSsyB8QhAyoxcpkECF5FoKaaa6AaZ5EkeZqX3KF'

@app.route('/')
def auth():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback='http://localhost:5000/')
    url = auth.get_authorization_url()
    return redirect(url)


if __name__ == '__main__':
    app.run()
