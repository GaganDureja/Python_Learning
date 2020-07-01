import mysql.connector

# Create connectionn to database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Password@123",
  database="students" #-- if no error means db exist
)

#create database

mycursor = mydb.cursor()
#mycur.execute("CREATE DATABASE students")

# list database
print("List of DataBase:")
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)

# create table
#mycursor.execute("CREATE TABLE students_info(student_id int primary key auto_increment, name varchar(25), address varchar(100) )")
# If table already exist use-- alter table students_info add column phone primary key

# list tables 
print("List of tables:")
mycursor.execute("SHOW TABLES")
for x in mycursor:
	print(x)

# Insert data

"""sql = "INSERT INTO students_info (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)""" #executemany- values are more than one

mydb.commit() # required to make changes otherwise no changes

print(mycursor.rowcount, "rows was inserted.") #total new rows inserted
print(mycursor.lastrowid) #shows the last inserted row id


# select all, where, order by

mycursor.execute("SELECT * FROM students_info WHERE student_id <= 10 ORDER BY name DESC") #top 10 results
myresult = mycursor.fetchall() #fetch data from last execute, fetchone() givest 1st output 
for x in myresult:
	print(x)
#use  WHERE address LIKE '%way%' -- o/p: highway, one way

# Delete 
"""sql = "DELETE FROM students_info WHERE address = %s"
adr = ("Mountain 21",)
mycursor.execute(sql, adr)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")"""

# DROP TABLE students_info/ DROP TABLE IF EXISTS students_info

# Update
# UPDATE stuents_info SET address = "new" WHERE address = "Mountain 21"
# don't forget about execute and commit and also use %s to prevent sql injection

# Limit -- the no of records
print("Another list with 5 limit and starting with the no 7")
sql = "SELECT * FROM students_info LIMIT 5 OFFSET 7"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
	print(x)

# Join Tables

print("2 Table joined results:")# backslash is used for code readability without cutting a line
sql = "SELECT \
       students_info.student_id AS Roll_no,\
       students_info.name AS Name,\
       branch.name AS Course\
       FROM students_info LEFT JOIN branch ON\
       branch.course_id = students_info.branch_id"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
	print(x)


#students_info and branch are table names