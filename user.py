import sqlite3

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
            return True
        else:
            return False 
    except sqlite3.Error as e:
        print('Error: ',e)
    finally:
        conn.close()