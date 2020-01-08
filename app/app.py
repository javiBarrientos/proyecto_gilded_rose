from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/inventario')
def inventario():
    return 'eis'


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
