import sqlite3
from flask import Flask,jsonify
import json
# Connect to SQLite database (creates if not exists)




def insertUserIntodb(first_name, last_name, date_of_birth, gender, email, occupation,bio, contact_details, home_address, postal_code, password, interests):
    query="INSERT INTO User (first_name, last_name, date_of_birth, gender, email, occupation,bio, contact_details, home_address, postal_code, password, interests)VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"
    conn = sqlite3.connect('comments.db')
    cursor = conn.cursor()
    try:
        cursor.execute(query, [ first_name, last_name, date_of_birth, gender, email, occupation,bio, contact_details, home_address, postal_code, password, interests])
        conn.commit()
    except sqlite3.Error as e:
        print('Error: ',e)
    finally:
        conn.close()



def loginCredentials(email, password):
    query="SELECT email,password from User WHERE email=? and password=?"
    conn = sqlite3.connect('comments.db')
    cursor = conn.cursor()
    try:
        cursor.execute(query, (email,password))
        credentials=cursor.fetchone()
        if credentials:
            return True
        else:
            return False
    except sqlite3.Error as e:
        print('Error: ',e)
    finally:
        conn.close()
        
        
        
        
def emailExists(email):
    query="SELECT email from User WHERE email=?"
    conn = sqlite3.connect('comments.db')
    cursor = conn.cursor()
    try:
        cursor.execute(query,(email,))
        user = cursor.fetchone()
        if user:
            return True
        else:
            return False 
    except sqlite3.Error as e:
        print('Error: ',e)
    finally:
        conn.close()
        
        
def selectAllfromUser(email):
    query="SELECT * from User WHERE email=?"
    conn = sqlite3.connect('comments.db')
    cursor = conn.cursor()
    try:
        cursor.execute(query,(email,))
        user = cursor.fetchone()
        
        if user:
            column=[column[0] for column in cursor.description]
            user_dict=dict(zip(column,user))
            user=user_dict
            return user
        else:
            return {'message':'email dont exist'}
    except sqlite3.Error as e:
        print('Error: ',e)
    finally:
        conn.close()
        
def insertBio(email,bio):
    query="UPDATE User SET bio=? WHERE email=?"
    conn = sqlite3.connect('comments.db')
    cursor = conn.cursor()
    try:
        cursor.execute(query,(bio,email))
        conn.commit()
    except sqlite3.Error as e:
        print('Error: ',e)
    finally:
        conn.close()
        
        
        
def insertContact(email,contact):
    query="UPDATE User SET contact_details=? WHERE email=?"
    conn = sqlite3.connect('comments.db')
    cursor = conn.cursor()
    try:
        cursor.execute(query,(contact,email))
        conn.commit()
    except sqlite3.Error as e:
        print('Error: ',e)
    finally:
        conn.close()
        
        
def insertAddress(email,address):
    query="UPDATE User SET home_address=? WHERE email=?"
    conn = sqlite3.connect('comments.db')
    cursor = conn.cursor()
    try:
        cursor.execute(query,(address,email))
        conn.commit()
    except sqlite3.Error as e:
        print('Error: ',e)
    finally:
        conn.close()
        
        
        
def insertPostal(email,postal_code):
    query="UPDATE User SET postal_code=? WHERE email=?"
    conn = sqlite3.connect('comments.db')
    cursor = conn.cursor()
    try:
        cursor.execute(query,(postal_code,email))
        conn.commit()
    except sqlite3.Error as e:
        print('Error: ',e)
    finally:
        conn.close()
        
        
        
def insertInterests(email,interests):
    query="UPDATE User SET interests=? WHERE email=?"
    conn = sqlite3.connect('comments.db')
    cursor = conn.cursor()
    try:
        cursor.execute(query,(interests,email))
        conn.commit()
    except sqlite3.Error as e:
        print('Error: ',e)
    finally:
        conn.close()

def insertImage(email,image):
    query="UPDATE User SET images=? WHERE email=?"
    conn = sqlite3.connect('comments.db')
    cursor = conn.cursor()
    try:
        cursor.execute(query,(image,email))
        conn.commit()
    except sqlite3.Error as e:
        print('Error: ',e)
    finally:
        conn.close()