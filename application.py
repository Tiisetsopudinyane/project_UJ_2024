from flask import Flask,redirect,url_for,render_template
from post import data,common_interests
from validation import encrypt_password

app=Flask(__name__)
@app.route("/")
def home():
    return render_template("posts.html",data=data)

@app.route("/login")
def login():
    return render_template("index.html")

@app.route("/createAccount")
def createAccount():
    return render_template("createAccount.html",common_interests=common_interests)
    
def password():
    return encrypt_password("password")

print("password ",password())



if __name__ =="__main__":
    app.run(debug=True)