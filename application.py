from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<HTML><HEAD></HEAD><BODY><h1>Hello World from Steffen!</h1></BODY>"