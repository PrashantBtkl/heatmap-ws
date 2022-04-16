import json
from flask import Flask
from flask_socketio import SocketIO

import db

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins=['http://127.0.0.1:1234','*'])

if __name__ == '__main__':
    socketio.run(app)

@socketio.on("click")
def store(pos):
    print("recieved click : ",pos)
    conn = db.get_conn()

    pos = json.loads(pos,)
    try:
        db.store_positions(pos, conn)
        print("successfully stored for page_id",pos["page_id"])
    except Exception as e:
        print("exception occured :", e)
    finally:
        conn.close()

@socketio.on("message")
def handle_message(data):
    print('received message: ' + data)

if __name__ == "__main__":
    print("Started heatmap-ws service")
    socketio.run(app)