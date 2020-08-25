import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    passwd = 'root',
    database = "testdatabase"
)

users = [("john", "jqthequick", "password", "jqthequick@gmail.com"),
        ("maura", "maura1", "password1", "maura@gmail.com"),
        ("dooter", "booter", "password12", "dooter@gmail.com"),
        ("lena", "blahblah", "password123", "lena@gmail.com"),
        ("schmidt", "kimmys", "password1234", "schmee@gmail.com"),
        ("scoobie", "doobie", "password0", "theCat@gmail.com")]

user_scores = [(98,80),
              (30,200),
              (67,178),
              (13,133),
              (4,100),
              (50,210)]
            
mycursor = db.cursor()
        
# q1 = "CREATE TABLE Users(id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), passwd VARCHAR(50))"
# q2 = "CREATE TABLE Scores (userId int PRIMARY KEY, FOREIGN KEY(userId) REFERENCES Users(id), game1 int DEFAULT 0, game2 int DEFAULT 0)"
# mycursor.execute(q1)
# mycursor.execute(q2)
# mycursor.execute("ALTER TABLE Users CHANGE passwd username VARCHAR(50)")
# mycursor.execute("ALTER TABLE Users ADD COLUMN passwd VARCHAR(50)")
# mycursor.execute("ALTER TABLE Users ADD COLUMN email VARCHAR(50)")

# q3 = "INSERT INTO Users (name, username, passwd, email) VALUES (%s, %s, %s, %s)"
# q4 = "INSERT INTO Scores (userId, game1, game2) VALUES (%s,%s,%s)"
# # mycursor.execute("SHOW TABLES")
# # for x in mycursor:
# #     print(x)

# for x, user in enumerate(users):
#     mycursor.execute(q3, user)
#     last_id = mycursor.lastrowid
#     mycursor.execute(q4, (last_id,) + user_scores[x])

db.commit()

mycursor.execute("SELECT * FROM Scores")
for x in mycursor:
    print(x)

mycursor.execute("SELECT * FROM Users")
for x in mycursor:
    print(x)