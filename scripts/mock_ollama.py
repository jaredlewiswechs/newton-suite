from flask import Flask, request, jsonify
import threading

app = Flask(__name__)


@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.get_json() or {}
    # Return a minimal plausible Ollama response
    response = {
        "id": "mock-1",
        "type": "response",
        "response": "{\"verdict\": \"UNCERTAIN\", \"confidence\": 5, \"reasoning\": \"mocked\"}",
    }
    return jsonify(response)


def run(host='0.0.0.0', port=11434):
    # Use threaded server so tests can call concurrently
    app.run(host=host, port=port, threaded=True)


if __name__ == '__main__':
    run()
