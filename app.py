from flask import Flask, redirect, url_for, render_template, request
from datetime import datetime

app = Flask(__name__) #Flask Constructor

# A decorator used to tell the application 
# which URL is associated function 

@app.route("/feed")  
def feed():
    posts_data = [
        {"username": "power_lifter", "content": "New PR today! 200kg Squat. Let's go!", "time": "12 MINS AGO", "type": "workout"},
        {"username": "fit_2012", "content": "Consistency is key. 30 days challenge done.", "time": "2 HOURS AGO", "type": "body"},
        {"username": "muscle_meals", "content": "Chicken and broccoli never tasted better.", "time": "5 HOURS AGO", "type": "food"}
    ]
    return render_template("feed.html", posts=posts_data)
    # 'posts' naam se data bhej rahe hain kyunki feed.html mein 'posts' likha hai
    return render_template("feed.html", posts=posts_data)

#Function is binded to the route
@app.route("/createProfile")
def create_profile():
    return render_template("create_profile.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/createPost")
def create_post():
    return render_template("create_post.html")

@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ =="__main__":
    app.run(debug=True)