from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def start_here():
     app = render_template("application-form.html")
     print app
     return app
#this step renders the HTML from the file onto the server site
#



if __name__ == "__main__":
    app.run(debug=True)