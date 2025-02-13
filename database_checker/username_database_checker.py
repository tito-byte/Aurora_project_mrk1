import sqlite3
import bcrypt
import os


report = None

def verify_password(stored_hash, entered_password):
    return bcrypt.checkpw(entered_password.encode(), stored_hash)

def login_user(username, password):
    conn = sqlite3.connect(r'/home/titobyte/Desktop/Databases/aurora_databases/aurora_userbase.sqlite')
    cursor = conn.cursor()

    # ✅ Fix column name quoting (use double quotes or square brackets)
    cursor.execute('SELECT "pass id" FROM "4uR0R4" WHERE username = ?', (username,))
    result = cursor.fetchone()


    conn.close()

    if result:
        stored_hash = result[0]

        # ✅ Ensure stored_hash is in bytes (needed for bcrypt)
        if isinstance(stored_hash, str):
            stored_hash = stored_hash.encode('utf-8')  # Convert string to bytes if necessary

        # ✅ Attempt password verification
        if verify_password(stored_hash, password):
            #print("✅ Login successful!")
            global report            
            report = 'yes'
            login_status()            
            
            
            
        else:
            #print("❌ Incorrect password.")
            
            report = 'no'
            login_status()

    else:
        #print("❌ Username not found.")
        report = 'nothing'
        login_status()

def login_status():

    if report == 'yes':
        status = "Login successful"
        return status
    
    if report == 'no':
        status = "Login unsuccessful"
        return status
    
    if report == 'nothing':
        status = "No user found"
        return status