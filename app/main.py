from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/run-pipeline')
def run_pipeline():
    """Endpoint that simulates the Run Pipeline action.
    Returns a JSON payload containing the welcome message that would be
    displayed in a modal popup on the client side.
    """
    return jsonify(message='welcome home')

if __name__ == '__main__':
    app.run()
