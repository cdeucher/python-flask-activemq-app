from stomp.listener import TestListener,WaitingListener
import stomp, json

class MyListener(stomp.ConnectionListener):
    def __init__(self, parent):
        self.conn = parent.conn
        self.parent = parent

    def on_error(self, frame):
        print('received an error "%s"' % frame.body)

    def on_message(self, frame):     
        req = json.loads(frame.body)
        items = [(k,v) for k,v in req.items()]      
        print('received a message "%s"' % req)
        if 'answer' in items[0]:
            self.parent.tip = frame.body       
            print('tip',self.parent.tip)
        elif 'msg' in items[0]:
            (msg,user) = req.items()
            print('msg',msg,user)
            if(msg[1] != ''):
                self.parent.words.append(msg[1])
            if(len(self.parent.words) >= 10):
                self.parent.words.pop(0)

    def on_disconnected(self):
        print('disconnected')
        self.parent.connect_and_subscribe()