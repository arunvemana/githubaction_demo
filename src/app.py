from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "This is index!testing"
    
@app.route('/test')
def index1():
    return "this is test2"


if __name__ == '__main__':
    app.run()
