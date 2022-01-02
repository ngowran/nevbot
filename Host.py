from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return 'Beep boop. nevbot is alive.'

def run():
    app.run(host='0.0.0.0', port=9090)

def host():
    server = Thread(target=run)
    server.start()