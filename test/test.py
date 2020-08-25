import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    passwd = 'root',
    database = "testdatabase"
)

mycursor = db.cursor()
# create table
# mycursor.execute("CREATE TABLE Test (name varchar(50) NOT NULL, created datetime NOT NULL, gender ENUM('M', 'F', 'O') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
# db.commit()

# add entry
# mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s,%s,%s)", ("Harry", datetime.now(), "M"))
# db.commit()

# query table
# mycursor.execute("SELECT id,name FROM Test WHERE gender = 'M' ORDER BY id DESC")

# # for x in mycursor:
#     print(x)

# add column
# mycursor.execute("ALTER TABLE Test ADD COLUMN food VARCHAR(50) NOT NULL")

# change column 
mycursor.execute("ALTER TABLE Test CHANGE name first_name VARCHAR(50)")

# display table
mycursor.execute("DESCRIBE Test")

for x in mycursor:
    print(x)

# remove column
# mycursor.execute("ALTER TABLE Test DROP food")

# db.commit()




