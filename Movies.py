from flask import Flask,jsonify,request
import csv

from flask.templating import render_template
all_movies = []
with open('movies.csv',encoding='utf8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
liked_movies = []
unliked_movies = []
didNot_watch = []
app = Flask(__name__)
@app.route('/get-Movies')
def get_Movies():
    return jsonify({
        'data':all_movies[1],
        'status':'succes'
    })

@app.route('/liked-Movie',methods=['POST'])
def liked_Movie():
    all_movies = [0]
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        'status':'succes'
    }),201 

@app.route('/unliked-Movie',methods=['POST'])
def unliked_Movie():
    all_movies = [0]
    movie = all_movies[0]
    all_movies = all_movies[1:]
    unliked_movies.append(movie)
    return jsonify({
        'status':'succes'
    }),201

@app.route('/notWatched-Movie',methods=['POST'])
def notWatched_Movie():
    all_movies = [0]
    movie = all_movies[0]
    all_movies = all_movies[1:]
    unliked_movies.append(movie)
    return jsonify({
        'status':'succes'
    }),201

if __name__ == '__main__':
    app.run()