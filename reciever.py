import requests
import time
from datetime import datetime

after = 0

def get_messages(after):
    response = requests.get(
        'http://127.0.0.1:5000/messages',
        params={'after': after}
    )
    data = response.json()
    return data['messages']

def print_message(message):
    username = message['username']
    message_time = message['time']
    text = message['text']

    dt = datetime.fromtimestamp(message_time)
    nice_time = dt.strftime('%H:%M:%S')

    print(nice_time, username)
    print(text + '\n')

while True:
    _messages = get_messages(after)

    if _messages:
        after = _messages[-1]['time']
        for message in _messages:
            print_message(message)


    time.sleep(1)
