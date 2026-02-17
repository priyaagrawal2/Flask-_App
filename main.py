import sqlite3

conn = sqlite3.connect("abc.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
""")

# cursor.execute(
#     "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
#     ("BOB", 22, "B+")
# )



# name = "Tom"

#web app form or sink
# Sqlite3 doesn't allow multiple sql statement to run , that's why it's safe
# name = "Tom); DROP TABLE students; --"
# cursor.execute(f"INSERT INTO students (name) VALUES ('{name}')")
#cursor.execute("insert into students (name,age,grade) values (?,?,?)",
#           ("BOB",22,"B+"))#This is the style to write parameterized query


# cursor.execute("SELECT * FROM students")
# rows = cursor.fetchall()

# print(rows)
# for row in rows:
#     print(rows)

# cursor.execute(f"INSERT INTO students (name) VALUES ('{name}')")
# cursor.execute("UPDATE students SET grade = ? WHERE id = ?",("A+",2))
# conn.commit()
student_1 = [
    ("abc",55,"B"),
    ("Bobthedog",33,"A"),
    ("abcd",26,"C")

]
# cursor.executemany("INSERT INTO students(name,age,grade) VALUES (?,?,?)",student_1)
# conn.commit()
# cursor.execute("SELECT * FROM students")



#DELETE DATA
# cursor.execute("DELETE FROM students WHERE id = ?",(4,))
# conn.commit()


# ORDER by
# cursor.execute("SELECT * FROM students ORDER BY age")
# cursor.execute("SELECT * FROM students ORDER BY age DESC")#for decending order
# cursor.execute("SELECT * FROM students")


#Delete duplicate rows
# cursor.execute("""
# DELETE FROM students
# WHERE id NOT IN (
#     SELECT MIN(id)
#     FROM students
#     GROUP BY name, age, grade
# )
# """)
# conn.commit()

#Find data by pattern like find all the name which has "om"
# cursor.execute("SELECT * FROM students WHERE name LIKE ?",("%om%",))

#Transaction and rollback

try:
    cursor.execute(
        "INSERT INTO students (name,age,grade) VALUES (?,?,?)",
        ("Raju",55,"B+")
    )
    raise Exception("error")
except:
    conn.rollback()
    print("rollback cancel the error query")


#Function to add the data 
def add_details(name,age,grade):
    cursor.execute("INSERT INTO students (name,age,grade) VALUES (?,?,?)",(name,age,grade))
    conn.commit()
    print("Data inserted")

add_details("BOBTHEDOG",11,"A")

#Function to delete the data
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print("data deleted")

    if cursor.rowcount == 0:
        print("No record found with this ID")
    else:
        print("Record deleted successfully")

#Function to show the data
def show_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if not rows:
        print("No data found")
    else:
        print("\nStudent Records:\n")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}")

show_students()


# rows = cursor.fetchall()
# for row in rows:
#     print(rows)
# # print(cursor.fetchmany(3))
# print(rows)
# conn.close()


