from flask import Flask, request, abort
import datetime
import time

app = Flask(__name__)

_messages = [
    {'username': 'Nick', 'text': 'Hello', 'time': 0.0}
]
_users = {
    'Nick': '12345'
}

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/status")
def status():
    return {
        'status': True,
        'name': "WriteMe",
        'users': len(_users),
        'messages': len(_messages),
        'time': datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    }

@app.route("/send", methods=['POST'])
def send():
    """
    -> JSON{
        "username": str,
        "password": str,
        "text": str
    }
    :return: JSON {'ok': true}
    """
    username = request.json['username']
    password = request.json['password']

    if username in _users: # registered user
        if password != _users[username]: # authorizing
            return abort(401)
    else: # new user
        _users[username] = password # adding new user

    text = request.json['text']
    current_time = time.time()
    message = {'username': username, 'text': text, 'time': current_time}
    _messages.append(message)

    print(_messages)

    return {'ok': True}

@app.route("/messages")
def messages():
    """
    -> ?after=float
    :return: JSON {
        "messages": [
            { "username": str, "text": str, "time": float }
            ...
        ]
    }
    """
    after = float((request.args.get('after')))

    filtered_messages = [message for message in _messages if message['time'] > after]

    return {
        'messages': filtered_messages
    }


app.run()