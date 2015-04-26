from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def start_here():
    return "Hi! this is the start of the application for Ubermelon"

@app.route("/uberapplicationstart")
def uber_applicationstart():

if __name__ == "__main__":
    app.run(debug=True)