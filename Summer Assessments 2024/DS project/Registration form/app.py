'''
from flask import Flask,render_template,request

from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="Kar@24092005"
app.config['MYSQL_DB']="registration_db"

mysql=MySQL(app)


@app.route('/',methods=['GET','POST'])
def index():

    if request.method == 'POST':
        username= request.form['username']
        email = request.form['email']
        

        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO user (n)")

    return render_template("register.html")

if __name__=="__main__":
    app.run(debug=True)
'''


from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "Kar@24092005"
app.config['MYSQL_DB'] = "registration_db"

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        student_name = request.form['student_name']
        father_name = request.form['father_name']
        mother_name = request.form['mother_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        date_of_birth = request.form['date_of_birth']
        address = request.form['address']
        blood_group = request.form['blood_group']
        department = request.form['department']
        course = request.form['course']
        password = generate_password_hash(request.form['password'])  # Hash password

        # Store data in the database
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (student_name, father_name, mother_name, phone_number, email, date_of_birth, address, blood_group, department, course, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (student_name, father_name, mother_name, phone_number, email, date_of_birth, address, blood_group, department, course, password))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('index'))  # Redirect to the root endpoint after registration

    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)
