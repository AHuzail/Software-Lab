from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello I am Huzail"

@app.route("/hello")
def hello():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)