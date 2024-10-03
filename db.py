import sqlite3


def init_db():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    # create table students
    cursor.execute('''
    create table if not exists students(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   student_name TEXT NOT NULL,
                   email TEXT NOT NULL,
                   currentclass REAL NOT NULL
    )
    ''')

    conn.commit()
    conn.close()


def add_student_details(student_name, email, currentclass):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute('insert into students (student_name, email, currentclass) values (?,?,?)',
                   (student_name, email, currentclass))
    conn.commit()
    conn.close()


def get_student_Details():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('select * from students')
    result = cursor.fetchall()  # Fetch all results from the query
    conn.close()
    return result
