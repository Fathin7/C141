from flask import Flask , jsonify , request
import csv
import pandas as pd
movies_data = pd.read_csv("final.csv")
app = Flask(__name__)
all_movies = movies_data[["original_title" , "poster_link" , "release_date" , "runtime" , "weighted_rating"]]
liked_movie = []
did_not_like_movie = []
did_not_watched_movies = []

def assign_val():
    m_data = {
        "original_title" : all_movies.iloc[0,0],
        "poster_link" : all_movies.iloc[0,1],
        "release_date" : all_movies.iloc[0,2],
        "duration" : all_movies.iloc[0,3],
        "rating" : all_movies.iloc[0,4]/2
    }
    return m_data

@app.route("/movies")

def get_movie():
    m_data = assign_val()
    return jsonify({
        "data" : m_data,
        "status" : "success"
    })

@app.route("/like")

def like_movies():
    global all_movies
    m_data = assign_val()
    liked_movie.append(m_data)
    all_movies.drop([0] , inplace = True)
    all_movies = all_movies.reset_index(drop = True)
    return jsonify({
        "status" : "success"
    })

@app.route("/liked")

def liked_m():
    global liked_movie
    return jsonify({
        "data" : liked_movie,
        "status" : "success"
    })

@app.route("/dislike")

def dislike_movies():
    global all_movies
    m_data = assign_val()
    did_not_like_movie.append(m_data)
    all_movies.drop([0] , inplace = True)
    all_movies = all_movies.reset_index(drop = True)
    return jsonify({
        "status" : "success"
    })

@app.route("/did_not_watch")

def did_not_watch():
    global all_movies
    m_data = assign_val()
    did_not_watched_movies.append(m_data)
    all_movies.drop([0] , inplace = True)
    all_movies = all_movies.reset_index(drop = True)
    return jsonify({
        "status" : "success"
    })

if __name__ == "__main__":
    app.run()