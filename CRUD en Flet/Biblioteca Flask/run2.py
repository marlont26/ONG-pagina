from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('connect')
def handle_connect():
    print("Client connected")

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")

@socketio.on('message')
def handle_message(data):
    try:
        print(f"Received message: {data}")
        # Enviar respuesta de vuelta al cliente
        emit('response', {'message': f"Server received: {data}"})
    except Exception as e:
        print(f"Error processing message: {e}")
        # Enviar un mensaje de error de vuelta al cliente
        emit('error', {'message': 'An error occurred while processing your message.'})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=80)