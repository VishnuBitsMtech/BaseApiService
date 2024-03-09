from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """Return index page."""
    return 'Sample Api Project!'

@app.route('/api')
def api():
    """Return API endpoint message."""
    return {'message': 'This is my API endpoint'}

if __name__ == '__main__':
    app.run(debug=True)
