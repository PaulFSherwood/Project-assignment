import mysql.connector
import bcrypt
import getpass

def execute_query(query, params=None):
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



# username1, password1 = "Anderson", bcrypt.hashpw("aaaa".encode(), bcrypt.gensalt())
username2, password2 = "Bailey", bcrypt.hashpw("bbbb".encode('utf-8'), bcrypt.gensalt())
# username3, password3 = "Carter", bcrypt.hashpw("cccc".encode(), bcrypt.gensalt())
# username4, password4 = "Davis", bcrypt.hashpw("dddd".encode(), bcrypt.gensalt())
# username5, password5 = "Edwards", bcrypt.hashpw("eeee".encode(), bcrypt.gensalt())
# username6, password6 = "Foster", bcrypt.hashpw("ffff".encode(), bcrypt.gensalt())
# username7, password7 = "Gray", bcrypt.hashpw("gggg".encode(), bcrypt.gensalt())
# username8, password8 = "Hughes", bcrypt.hashpw("hhhh".encode(), bcrypt.gensalt())
# username9, password9 = "Jenkins", bcrypt.hashpw("jjjj".encode(), bcrypt.gensalt())
# username10, password10 = "King", bcrypt.hashpw("kkkk".encode(), bcrypt.gensalt())

# print(password1)
print(password2)
# print(password3)
# print(password4)
# print(password5)
# print(password6)
# print(password7)
# print(password8)
# print(password9)
# print(password10)

print(f"Hashed password: {password2}")

# # update all the users passwords in the database
# for i in range(1, 10):
#     execute_query("""
#     UPDATE users
#     SET password = ?
#     WHERE username = ?
#     """, (locals()[f"password{i}"], locals()[f"username{i}"]))

# get username
username = input("Enter your username: ")
# get password and convert
userPassword = getpass.getpass("Enter your password: ")
# Hash the pass
password_hashed = bcrypt.hashpw(userPassword.encode(), bcrypt.gensalt())

# save query to variable
query = "SELECT * FROM users WHERE username = %s AND password = %s"
params = (username, password_hashed)

# try query and save the result
result = execute_query(query, params)

# test if the login works
if len(result) > 0:
    print("Login successful")
    for i in result:
        print(i)
else:
    print("Login failed")