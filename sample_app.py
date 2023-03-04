"""Sample Flask app for testing purposes."""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    """Return a simple string response."""
    return 'Hello, World!'

@app.route('/test')
def test():
    """Return a simple JSON response."""
    return {'test_response': 'This is a test'}
