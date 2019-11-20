from flask import Flask, Session, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def hello():
    return "Hello World!"

app.run(debug= True)
