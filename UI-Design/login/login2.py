import mysql.connector
import hashlib

def execute_query(self, query, params=None):
    # Connection to the flight sim database
    db = mysql.connector.connect(
        host='localhost',
        user='sherwood',
        password='sherwood',
        database='flight_simulator_db'
    )
    # Create the cursor for the look in the db
    cursor = db.cursor()
    # Execute the query passed in by the user / function
    if params is not None:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    # save the result
    result = cursor.fetchall()
    # close the connection
    cursor.close()
    db.close()
    return result

# cur.execute("""
# CREATE"""

# username1, password1 = "Bailey", hashlib.sha256("1234".encode()).hexdigest()

# print(username1, password1)

username1, password1 = "Anderson", hashlib.sha256("aaaa".encode()).hexdigest()
username2, password2 = "Bailey", hashlib.sha256("bbbb".encode()).hexdigest()
username3, password3 = "Carter", hashlib.sha256("cccc".encode()).hexdigest()
username4, password4 = "Davis", hashlib.sha256("dddd".encode()).hexdigest()
username5, password5 = "Edwards", hashlib.sha256("eeee".encode()).hexdigest()
username6, password6 = "Foster", hashlib.sha256("ffff".encode()).hexdigest()
username7, password7 = "Gray", hashlib.sha256("gggg".encode()).hexdigest()
username8, password8 = "Hughes", hashlib.sha256("hhhh".encode()).hexdigest()
username9, password9 = "Jenkins", hashlib.sha256("jjjj".encode()).hexdigest()
username10, password10 = "King", hashlib.sha256("kkkk".encode()).hexdigest()

# update all the users passwords in the database
for i in range(1, 10):
    execute_query("""
    UPDATE users
    SET password = ?
    WHERE username = ?
    """, (locals()[f"password{i}"], locals()[f"username{i}"]))
    