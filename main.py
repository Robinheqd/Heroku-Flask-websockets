from flask import Flask
from flask_sockets import Sockets

app = Flask(__name__)
sockets = Sockets(app)

@sockets.route("/echo")
def echo_socket(ws):
  while not ws.closed:
    message = ws.receive()
    ws.send(message)
