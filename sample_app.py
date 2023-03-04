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

@app.route('/test_int')
def test_int():
    """Return a simple integer response."""
    return 1

@app.route('/test_list')
def test_list():
    """Return a simple list response."""
    return [1, 2, 3]

if __name__ == '__main__':
    app.run()
