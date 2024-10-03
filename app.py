from flask import Flask, session, jsonify, request
import sqlite3
from db import init_db, add_student_details, get_student_Details

init_db()

app = Flask(__name__)
app.secret_key = 'demo'


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user_id = data.get('user_id', 0)
    session['user_id'] = user_id
    print(data)
    return jsonify({"message": "This data is now stored in the session"}), 200


@app.route('/student/add', methods=['POST'])
def add_student():  # question 4 session = session ['user_id] if else
    data = request.get_json()
    student_name = data.get('student_name')
    email = data.get('email', 'No@email.com')
    currentclass = data.get('currentclass', 'someclass')
    add_student_details(student_name, email, currentclass)
    return jsonify({"message": "student added successfully"}), 201


@app.route('/student/list', methods=['GET'])
def get_students():
    result = get_student_Details()
    return jsonify({"data": result}), 200
