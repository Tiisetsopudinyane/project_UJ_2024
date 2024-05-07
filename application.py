from flask import Flask,redirect,url_for,render_template,request,jsonify,session
from post import data,common_interests,logindetails
from validation import matchPassword,encrypt_password
from user import insertUserIntodb,loginCredentials,emailExists,selectAllfromUser,insertBio,insertContact,insertAddress,insertPostal,insertInterests

app=Flask(__name__)
app.secret_key="session"
@app.route("/")
def homePage():
    user=selectUserInfo()
    return render_template("userProfile.html",user=user,data=data)



@app.route("/loginpage")
def login():
    return render_template("index.html")


@app.route("/login",methods=['POST'])
def login_in():
    if request.method=="POST":
        email=request.form["email"]
        password=request.form["password"]
        
        password=encrypt_password(password.strip())
        user_credentials=loginCredentials(email,password)
        
        if user_credentials:
            session["email"]=email
            user=selectUserInfo()
            return render_template("userProfile.html",user=user,data=data)
        else:
            return "email or password not correct"
    return render_template("index.html")


@app.route("/logout",methods=['POST'])
def logout():
    session.clear()
    return render_template("index.html")

@app.route("/autologout")
def autologout():
    session.clear()
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
    bio=request.form.get('bio')
    contact = request.form.get('contact')
    address = request.form.get('address')
    postalCode = request.form.get('postalCode')
    password = request.form.get('password')
    confirmPassword = request.form.get('confirmPassword')
    interest = request.form.get('interest')

    # Check if password and confirm password match
    finalPassword = matchPassword(password.strip(), confirmPassword.strip())
    
    # Check if the email already exist in the database
    emailExistance=emailExists(email)
    
    if not emailExistance:
        insertUserIntodb( firstName, lastName, dob, gender, email, occupation,bio, contact, address, postalCode, finalPassword, interest)
        session["email"]=email
        return redirect(url_for("homePage"))
    else:
        return jsonify({'message':'This email already registered to an account'})
    #jsonify({'message': 'Form submitted successfully'})


@app.route('/userprofileEdit')
def userprofileedit():
    return render_template('userprofileEdit.html')




@app.route('/updateUserInfo',methods=['POST'])
def updateUser():
    email=session['email']
    bio=request.form.get('bio')
    contact=request.form.get('contact')
    address=request.form.get('address')
    postal_code=request.form.get('postalCode')
    interests=request.fomr.get('interest')
    if bio:
        insertBio(email,bio)
    if contact:
        insertContact(email,contact)
    if address:
        insertAddress(email,address)
    if postal:
        insertPostal(email,postal_code)
    if interests:
        insertInterests(email,interests)
            
        


@app.route('/userinfo')
def selectUserInfo():
    if "email" in session:
        userEmail=session["email"]
        user=selectAllfromUser(userEmail)
        return user
    
    


    

    

if __name__ =="__main__":
    app.run(debug=True)