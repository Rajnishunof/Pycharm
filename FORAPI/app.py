from flask import Flask
from mysql.connector import connect

app = Flask(__name__)

# MySQL configurations


@app.route('/')
def index():
   return "hello"

if __name__ == '__main__':
    app.run(debug=True)
