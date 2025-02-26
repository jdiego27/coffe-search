from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data for coffee shops (This can be replaced with a database)
coffee_shops = [
    {"name": "Java Brew", "location": "Downtown", "rating": 4.5},
    {"name": "Cafe Mocha", "location": "Uptown", "rating": 4.0},
    {"name": "The Bean Spot", "location": "Midtown", "rating": 4.8},
    {"name": "Café Latte", "location": "West End", "rating": 3.9},
]

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


if __name__ == "__main__":
    app.run(debug=True)
