"""
from ws4py.websocket import WebSocket

class EchoWebSocket(WebSocket):
    def received_message(self, message):
        self.send(message.data, message.is_binary)

sever = EchoWebSocket('ws://localhost:9000/')

print "asd"
"""

import tweepy


auth = tweepy.OAuthHandler('L5njVc0ncYBtytQUzOMYyp9L5', 'IzmMZUSqQmtw5QGDasaGCi7szM5ZPMxa6l3FuqgZHUN6nTmlW1')
auth.set_access_token('2999060529-k0outcMZ6Me9rBe8FPgqUS4vpJxFfDOt1o3zQ16', '5umm0LbUFLXYllJisQAvjjKKWLkqqx0WDxEmBvabKkqUG')
api = tweepy.API(auth)

def user(id):
    response = api.get_user(id)
    return response

def search(q,lat,lng,km):
    t = str(lat)+','+str(lng)+','+str(km)+'km'
    response = api.search(q,geocode=t,rpp=100)
    return response
