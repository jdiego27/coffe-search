from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

app = Flask(__name__)

'''
# Add data base REMOTE
#app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:rootuser@localhost/coffee_database'

def get_db_connection():
    connection = mysql.connector.connect(
        host='jdleonr.mysql.pythonanywhere-services.com',  # e.g., 'localhost'
        user='jdleonr',  # e.g., 'root'
        password='rootuser',
        database='jdleonr$coffee_database'
    )
    return connection

'''
# Add data base LOCAL
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',  # e.g., 'localhost'
        user='root',  # e.g., 'root'
        password='rootuser',
        database='coffee_database'
    )
    return connection

@app.route('/api', methods=['GET'])
def get_coffees():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)  # This will return rows as dictionaries

    query = "SELECT * FROM coffee_shop;"
    cursor.execute(query)

    coffees = cursor.fetchall()  # Retrieve all rows
    cursor.close()
    connection.close()

    return jsonify(coffees)  # Return as a JSON response

@app.route('/', methods=['GET', 'POST'])
def home():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)  # This will return rows as dictionaries

    query = "SELECT * FROM coffee_shop;"
    cursor.execute(query)

    coffees = cursor.fetchall()  # Retrieve all rows
    cursor.close()
    connection.close()

    return render_template('home.html', coffees=coffees)


if __name__ == "__main__":
    app.run(debug=True)