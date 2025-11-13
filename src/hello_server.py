from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World", 200

app.run("0.0.0.0", 5000)
