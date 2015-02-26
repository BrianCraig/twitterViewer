import tweepy

from .settings import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def user(id):
    response = api.get_user(id)
    return response


def search(q, lat, lng, km):
    t = str(lat) + ',' + str(lng) + ',' + str(km) + 'km'
    response = api.search(q, geocode=t, rpp=100)
    return response
