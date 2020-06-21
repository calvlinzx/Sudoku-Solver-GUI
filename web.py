from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/calvin')
def calvin():
    return 'Hi Calvin'


if __name__ == '__main__':
    app.run()
