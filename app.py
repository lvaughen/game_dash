
from flask import Flask, jsonify, render_template
from flask_pymongo import PyMongo
from os import environ
 
app = Flask(__name__)
 
app.config['MONGO_URI'] = environ.get('MONGODB_URI','mongodb://localhost:27017/games_db')

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')
 

@app.route('/api/ms_rank')
def getMsRanks():
    tasks = mongo.db.ms_games.find({})
    data = []
    print(tasks)

    for task in tasks:
        item = {
            'id': str(task['_id']),
            'date': task['Date'],
            'country': task['Country'],
            'rank': task['Rank'],
            'game': task['Game'],
            'Image': task['Image']
        }
        data.append(item)

    return jsonify(data)


@app.route('/api/ms_games_detail')
def getMsGameDetail():
    tasks = mongo.db.ms_games_detail.find({})
    data = []
    print(tasks)

    for task in tasks:
        item = {
            'id': str(task['_id']),
            'date': task['Date'],
            'game': task['Game'],
            'descrip': task['Description'],
            'rating': task['Rating'],
            'rating_notes': task['Rating Notes'],            
            'screens': task['Screen Links']
        }
        data.append(item)

    return jsonify(data)


if  __name__ == '__main__':
        app.run(debug=True)