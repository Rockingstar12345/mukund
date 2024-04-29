from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def show_students():
    students=[
        {"name":"Alice", "grade":85},
        {"name":"Bob","grade":72},
        {"name":"Charlie","grade":95},
        {"name":"Daisy","grade":60},
        {"name":"Eve","grade":50},
    ]
    passing_grade=80
    return  render_template('grade.html',students=students,passing_grade=passing_grade)
app.run()