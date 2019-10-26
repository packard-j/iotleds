from flask import Flask
from flask_socketio import SocketIO
# from iotleds.bridge.server import MessageServer
# from iotleds.bridge.message import Message, SolidColor

# ms = MessageServer()
print("Waiting for LED connection...")
# ms.connect()

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@socketio.on('color')
def handle_color(color):
    scale = 100 / (color['r'] + color['g'] + color['b'])
    msg = (int(color['r'] * scale),
                      int(color['g'] * scale),
                      int(color['b'] * scale))
    #ms.send(msg)
    print(msg)


if __name__ == '__main__':
    socketio.run(app)
