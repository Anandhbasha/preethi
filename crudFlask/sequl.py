# pip install mysql-connector-python
import mysql.connector
# connect Db
mydb = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password="",
    database = "newdb"
)

cursor = mydb.cursor()

# create Table
# cursor.execute("""CREATE TABLE IF NOT EXISTS users(
# id INT AUTO_INCREMENT PRIMARY KEY,
# name VARCHAR(100),
# age INT
# )""")

# print("Table is created")

# insert Data
# sql = "INSERT INTO users (name,age) VALUES(%s,%s)"
# val = ("XYZ",25)
# cursor.execute(sql,val)
# mydb.commit()
# print("Inserted",cursor.rowcount)

# read
# cursor.execute("SELECT * FROM users")
# for row in cursor.fetchall():
#     print(row)

# update
sql = "UPDATE users SET age=%s WHERE id=%s" 
val = (30,1)
cursor.execute(sql,val)
mydb.commit()
print("Update Succesfully")

# Delete
sql = "DELETE FROM users WHERE id=%s"
val=(1,)
cursor.execute(sql,val)
mydb.commit()
print("User Deleted Succesfully")
