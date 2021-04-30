import os
from flask import Flask, request, render_template,  send_file, json, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin

#class router():
#    def __init__(self):    
__TEMPLATE_PATH__=os.getcwd()+"/src/activemqapp/templates/vue/client/dist"

flaskApp = Flask(__name__, template_folder=__TEMPLATE_PATH__)
api = Api(flaskApp)
CORS(flaskApp, resources={r"/*": {"origins": "*"}})

@flaskApp.route('/')
def catch_all():
    return render_template("/index.html")

@flaskApp.route('/files', defaults={'req_path': ''})
@flaskApp.route('/files/<path:req_path>')
def files_page(req_path):     
    abs_path = os.path.join(__TEMPLATE_PATH__, req_path)
    if not os.path.exists(abs_path):
        print(abs_path)
        return 503
    if os.path.isfile(abs_path):
        return send_file(abs_path) 

@flaskApp.route('/msg', methods=['GET','POST'])
def msg():
    localTip = json.loads(flaskApp.appRunner.tip)    
    localTip['answer'] = ''
    localTip['list'] = flaskApp.appRunner.words
    response = json.dumps(localTip)
    print('msg',response)
    return response

@flaskApp.route('/word', methods=['GET','POST'])
def word():
    req = request.json
    req = json.loads(json.dumps(req))
    localTip = json.loads(flaskApp.appRunner.tip)

    if (req['msg'] == localTip['answer']):
        localTip['winner']=req['user']
        flaskApp.appRunner.tip = json.dumps(localTip)

    localTip['answer']=''

    flaskApp.appRunner.conn.send('/topic/'+flaskApp.appRunner.QUEUE_NAME, '{"msg":"'+req['msg']+'","user":"'+req['user']+'"}')
    return json.dumps(localTip)