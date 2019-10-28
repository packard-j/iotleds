from flask import Flask, render_template
from flask_socketio import SocketIO
from iotleds.bridge.server import MessageServer
from iotleds.bridge.message import SolidColor, Rainbow

ms = MessageServer()
print("Waiting for LED connection...")
ms.connect()
print("Connected!")

app = Flask(__name__, static_folder="build/static", template_folder="build")
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/rainbow')
def rainbow():
    msg = Rainbow()
    ms.send(msg)
    return "ok"


@socketio.on('color')
def handle_color(color):
    msg = SolidColor((int(color['r']*100/765),
                      int(color['g']*100/765),
                      int(color['b']*100/765)))
    ms.send(msg)
    print(msg)


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0")
