import time
from datetime import datetime

from flask import Flask, request

app = Flask(__name__)
database = [
    {
     'time': time.time(),
     'name': 'Jack',
     'text': 'Привет всем!',
     },
    {
     'time': time.time(),
     'name': 'Mary',
     'text': 'Привет, Jack!',
     },
] #база данных

@app.route("/status")
def status():
    dt_now = datetime.now()
    return {
        'status': True,
        'name': 'Mesenger',
        'time1': time.asctime(),
        'time2': time.time(),
        'time3': dt_now,
        'time4': str(dt_now),
        'time5': dt_now.strftime('%Y/%m/%d time: %H:%M:%S'),
        'time3': dt_now.isoformat(),
    }

@app.route("/send", methods=['POST'])
def send_message():
    data = request.json
    name = data['name']
    text = data['text']


        message = {
            'time': time.time(),
            'name': name,
            'text': text,
        }
        database.append(message)
    return {'ok': True}
@app.route("/messages")
def get_messages():
    result = []
    for message in database:
        if message['time'] > after:
            result.append(message)
    return result


return {'ok': True}
app.run()