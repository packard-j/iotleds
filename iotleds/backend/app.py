from flask import Flask, request, render_template
from flask_socketio import SocketIO
from iotleds.bridge.server import MessageServer
from iotleds.bridge.message import *

ms = MessageServer()
print("Waiting for LED connection...")
ms.connect()
print("Connected!")

app = Flask(__name__, static_folder="build/static", template_folder="build")
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/pattern', methods=['POST'])
def pattern():
    if not request.is_json:
        return "request invalid"
    data = request.get_json()
    print(data)
    c1 = (int(data['c1']['r'] * 100 / 765),
          int(data['c1']['g'] * 100 / 765),
          int(data['c1']['b'] * 100 / 765))
    c2 = (int(data['c2']['r'] * 100 / 765),
          int(data['c2']['g'] * 100 / 765),
          int(data['c2']['b'] * 100 / 765))
    speed = max(min(int(data['speed']), 10), 1)
    n = max(min(int(data['n']), 25), 1)
    msg = Pattern((c1, c2), n, speed)
    ms.send(msg)
    return "ok"


@app.route('/rainbow')
def rainbow():
    msg = Rainbow()
    ms.send(msg)
    return "ok"


@socketio.on('color')
def handle_color(color):
    c = (int(color['r']*100/765),
         int(color['g']*100/765),
         int(color['b']*100/765))
    ms.send(SolidColor(c))


@socketio.on('cascade')
def handle_cascade(cascade):
    color = cascade.get('color')
    c = None
    if color:
        c = (int(color['r'] * 100 / 765),
             int(color['g'] * 100 / 765),
             int(color['b'] * 100 / 765))
    loop = cascade.get('loop')
    ms.send(Cascade(c, loop))


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0")
