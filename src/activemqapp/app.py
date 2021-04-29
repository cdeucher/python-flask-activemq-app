import os, time
import stomp

from src.activemqapp.routes.router import *
from src.activemqapp.mq.mq import *

class app:
    def __init__(self):
        self.tip='{"answer":"hello","word":5,"tip":"new tip for 5 ?","winner":""}' 
        self.words=[]
        self.QUEUE_NAME='XYZ'
        self.conn = stomp.Connection([('activemq', 61613)])#, heartbeats=(4000, 4000))
        self.conn.set_listener('', MyListener(self))        
        self.connect_and_subscribe()

        self.run()

    def connect_and_subscribe(self):
            print('connect_and_subscribe')
            self.conn.connect(wait=True)
            self.conn.subscribe(destination='/topic/'+self.QUEUE_NAME, id=1, ack='auto') 

    def run(self):
        global flaskApp
        flaskApp.appRunner=self
        flaskApp.run(host="0.0.0.0", port=8080, debug=True)
        self.conn.unsubscribe(1)
        self.conn.disconnect()