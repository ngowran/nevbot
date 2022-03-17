from flask import Flask
from threading import Thread

app = Flask('')

#returns a message in the terminal if the start up is sucessful;
@app.route('/')
def main():
    return 'Beep boop. nevbot is alive.'

#sets the port the server will run on
def run():
    app.run(host='0.0.0.0', port=9090)

#starts the server
def host():
    server = Thread(target=run)
    server.start()