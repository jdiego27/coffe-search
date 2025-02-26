from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

app = Flask(__name__)

# Add data base
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:rootuser@localhost/coffee_database'

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',  # e.g., 'localhost'
        user='root',  # e.g., 'root'
        password='rootuser',
        database='coffee_database'
    )
    return connection

"""
# Sample data for coffee shops (This can be replaced with a database)
coffee_shops = [
    {"name": "Java Brew", "location": "Downtown", "rating": 4.5, "image" : "static/coffee1.jpg"},
    {"name": "Cafe Mocha", "location": "Uptown", "rating": 4.0, "image" : "static/coffee2.jpg"},
    {"name": "The Bean Spot", "location": "Midtown", "rating": 4.8, "image" : "static/coffee1.jpg"},
    {"name": "Café Latte", "location": "West End", "rating": 3.9, "image" : "static/coffee1.jpg"},
    {"name": "Café Latte", "location": "West End", "rating": 3.9, "image" : "static/coffee1.jpg"},
    {"name": "Café Latte", "location": "West End", "rating": 3.9, "image" : "static/coffee1.jpg"},
]
"""

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

@app.route('/', methods=['GET'])
def home():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)  # This will return rows as dictionaries

    query = "SELECT * FROM coffee_shop;"
    cursor.execute(query)

    coffees = cursor.fetchall()  # Retrieve all rows
    cursor.close()
    connection.close()

    return render_template('home.html', coffees=coffees)



"""
@app.route('/', methods=['GET', 'POST'])
def home():
    search_location = request.form.get('location')
    search_rating = request.form.get('rating')
    
    # Filter the coffee shops based on the search criteria
    filtered_shops = coffee_shops
    if search_location:
        filtered_shops = [shop for shop in filtered_shops if search_location.lower() in shop['location'].lower()]
    if search_rating:
        filtered_shops = [shop for shop in filtered_shops if shop['rating'] >= float(search_rating)]
    
    return render_template('home.html', coffee_shops=filtered_shops)
"""

if __name__ == "__main__":
    app.run(debug=True)
