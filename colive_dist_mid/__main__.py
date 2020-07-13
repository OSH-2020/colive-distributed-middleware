import socketio
from flask import Flask

from .sio import sio


def main():
    flask_app = Flask(__name__)
    flask_app.wsgi_app = socketio.WSGIApp(sio, flask_app.wsgi_app)
    flask_app.run('127.0.0.1', 2000)


if __name__ == '__main__':
    main()
