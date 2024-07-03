from flask import Flask, jsonify, request
import time

app = Flask(__name__)
clients = {}
TIMEOUT = 60  # Timeout period in seconds

@app.route('/')
def home():
    current_time = time.time()
    active_clients = {client: last_seen for client, last_seen in clients.items() if current_time - last_seen < TIMEOUT}
    total_clients = len(active_clients)
    return jsonify({"total_clients": total_clients, "clients": active_clients})

@app.route('/ping', methods=['POST'])
def ping():
    client_id = request.json.get('client_id')
    clients[client_id] = time.time()
    return '', 204

@app.route('/clients')
def get_clients():
    current_time = time.time()
    active_clients = {client: last_seen for client, last_seen in clients.items() if current_time - last_seen < TIMEOUT}
    return jsonify(active_clients)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
