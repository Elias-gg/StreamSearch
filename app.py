import os
import flask
import flask_socketio
import requests
from flask import Flask, render_template
from flask_socketio import SocketIO
import chill
import certifi


import requests

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)
messages = []
#Guidebox API Key c338d925a0672acf243133ddc1d5d66fb0191391
#http://api-public.guidebox.com/v1.43/ {region} / {api key}
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return flask.render_template('index.html')
   
@app.route('/shows')
def hello2():
    return flask.render_template('index.html')

@app.route('/movies')
def hello3():
    return flask.render_template('index.html')

@socketio.on('connect')
def on_connect():
    print('Client connected')
    
@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')
@socketio.on('login')
def get_token(data):
    print(data['token'])
    
@socketio.on('new message')
def on_new_message(data):
    
    print data['message']
    messages.append({
                    'message': "Me: " + data['message']
                })
    socketio.emit('all messages',{'messages': messages})
    mes = chill.get_chatbot_response(data['message'])
    print mes
    messages.append({
                    'message': str(mes['message'])
                })

    socketio.emit('all messages',{'messages': messages})
    print "done"
    
    
@socketio.on('search1')
def onSearch(data):
    #print data
    #print "here"
    print ""
 
if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )