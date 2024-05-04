from flask import Flask,redirect,url_for,render_template,request,jsonify
from post import data,common_interests
from validation import matchPassword

app=Flask(__name__)
@app.route("/")
def home():
    return render_template("userProfile.html",data=data)

@app.route("/login")
def login():
    return render_template("index.html")

#route to the create account page
@app.route("/createAccount")
def createAccount():
    return render_template("createAccount.html",common_interests=common_interests)

#route to post the users info
@app.route("/AccountCreation", methods=['POST'])
def account_creation():
    firstName = request.form.get('firstName')
    lastName = request.form.get('lastName')
    dob = request.form.get('dob')
    gender = request.form.get('gender')
    email = request.form.get('email')
    occupation = request.form.get('occupation')
    contact = request.form.get('contact')
    address = request.form.get('address')
    postalCode = request.form.get('postalCode')
    password = request.form.get('password')
    confirmPassword = request.form.get('confirmPassword')
    interest = request.form.get('interest')

    # Check if password and confirm password match
    finalPassword = matchPassword(password, confirmPassword)
    #if finalPassword is None:
        #return jsonify({'error': 'Passwords do not match'}), 400
    print(finalPassword)
    #print(interest)
    return jsonify({'message': 'Form submitted successfully'})



if __name__ =="__main__":
    app.run(debug=True)