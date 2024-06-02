import mysql.connector
from typing import List, Tuple

db = mysql.connector.connect(host="localhost", user="root", passwd="1111")

cursor = db.cursor()
# cursor.execute("SHOW DATABASES")
# result = cursor.fetchall()
# for database in result:
#     print(database)
try:
    cursor.execute("USE testdb")
    print("Connected to testdb")
except mysql.connector.Error as e:
    print(f"Cannot Connect to testdb {e}")

# customer = cursor.execute(
#     """CREATE TABLE IF NOT EXISTS customer(
#         id INT AUTO_INCREMENT,
#         name VARCHAR(35) NOT NULL,
#         city VARCHAR(15) NOT NULL,

#         CONSTRAINT ID_PK PRIMARY KEY (id)
#     )
#     """
# )

# try:
#     cursor.execute(
#         "INSERT INTO customer (name, city) VALUES (%s, %s)", ("John Doe", "New York")
#     )
#     cursor.execute(
#         "INSERT INTO customer (name, city) VALUES (%s, %s)",
#         ("Jane Smith", "Los Angeles"),
#     )
#     db.commit()  # Commit the transaction
#     print("Sample data inserted into 'customer' table.")
# except mysql.connector.Error as err:
#     print(f"Failed to insert data: {err}")

# try:
#     students = cursor.execute(
#         """
#             CREATE TABLE IF NOT EXISTS student(
#                 `id` INTEGER AUTO_INCREMENT,
#                 `name` VARCHAR(50) NOT NULL,
#                 `major` VARCHAR(15) NOT NULL,
#                 `current year` INTEGER CHECK(`current year` BETWEEN 1 AND 5) ,

#                 CONSTRAINT STUDENT_PK PRIMARY KEY (id)
#         )"""
#     )
#     print("table created successfully")
# except mysql.connector.Error as e:
#     print(f"Cannot create the table {e}")

# try:
#     students_list: List[Tuple[str, str, int]] = [
#         ("ahmed", "Data scientist", 2),
#         ("mohamed", "accountant", 1),  # Changed year from 15 to 1 for valid range
#         ("yassien", "Real Estate", 2)
#     ]

#     insertion_query = "INSERT INTO student (name, major, `current year`) VALUES (%s, %s, %s)"
#     cursor.executemany(insertion_query, students_list)
#     db.commit()  # Commit the transaction
#     print("Sample data inserted into 'student' table successfully.")
# except mysql.connector.Error as e:
#     print(f"Cannot add student_list to table: {e}")

try:
    query_2 = "SELECT * from student"
    cursor.execute(query_2)
    result = cursor.fetchall()

    for student in result:
        print(student)

except mysql.connector.Error as e:
    print(f"Cannot print the student table {e}")

print("\n", "-"*30)
query = "SELECT * FROM student WHERE `name` like '%d'"

cursor.execute(query)
startswith_s = cursor.fetchall()
for i in startswith_s:
    print(i)

print("\n", "-"*30)
updated_table = "UPDATE student SET `current year` = 5 WHERE name = 'mohamed'"
cursor.execute(updated_table)
db.commit()


cursor.execute(query_2)
table = cursor.fetchmany(2)
for i in table:
    print(i)
