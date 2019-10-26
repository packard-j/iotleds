from flask import Flask, render_template
from flask_socketio import SocketIO
from iotleds.bridge.server import MessageServer
from iotleds.bridge.message import SolidColor

ms = MessageServer()
print("Waiting for LED connection...")
ms.connect()

app = Flask(__name__, static_folder="build/static", template_folder="build")
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template("index.html")


@socketio.on('color')
def handle_color(color):
    scale = 100 / (color['r'] + color['g'] + color['b'])
    msg = SolidColor((int(color['r'] * scale),
                      int(color['g'] * scale),
                      int(color['b'] * scale)))
    ms.send(msg)
    print(msg)


if __name__ == '__main__':
    socketio.run(app)
