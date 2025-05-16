from flask import Flask, request, render_template
import requests

app = Flask(__name__)

THEMEALDB_SEARCH_URL = "https://www.themealdb.com/api/json/v1/1/filter.php"
THEMEALDB_LOOKUP_URL = "https://www.themealdb.com/api/json/v1/1/lookup.php"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    ingredients = request.args.get('ingredients')
    if not ingredients:
        return render_template('index.html', recipes=[])

    # Use only the first ingredient (API supports one at a time)
    ingredient = ingredients.split(',')[0].strip()
    params = {'i': ingredient}
    res = requests.get(THEMEALDB_SEARCH_URL, params=params)
    data = res.json()

    meals = data.get('meals', [])
    return render_template('index.html', recipes=meals)

@app.route('/recipe/<meal_id>')
def recipe_detail(meal_id):
    res = requests.get(THEMEALDB_LOOKUP_URL, params={'i': meal_id})
    data = res.json()
    recipe = data['meals'][0] if data['meals'] else None
    return render_template('recipe.html', recipe=recipe)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

