# C:\DevOps\30juneTest\code.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello sir, i have completed my task till here .'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)