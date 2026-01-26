from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/post")
def post():
    return render_template("post.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/create")
def create_post():
    return render_template("create.html")

if __name__ =="__main__":
    app.run(debug=True)