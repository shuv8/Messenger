from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, world!"

@app.route("/status")
def status():
    return {
        'status': True,
        'name': "WriteMe",
        'time': datetime.datetime.now()
    }

app.run()