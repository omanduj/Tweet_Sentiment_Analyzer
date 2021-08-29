from flask import Flask, url_for, render_template, request, jsonify
from markupsafe import escape, Markup
import yaml
from test_flask.my_project.pythonAPY_ import main_API_one, create_twitter_url, main_API_two
from test_flask.my_project.database import main_DB, select_info



app = Flask(__name__)

@app.route("/tweetanalysis/", methods = ["POST"])
#CURL STUFF
def main():
    some_json = request.get_json()
    username = some_json["username"]
    count = some_json["num_of_tweets"]
    emotions = main_API_one(username, count)
    pos_emotion = emotions["pos"]
    neg_emotion = emotions["neg"]
    neu_emotion = emotions["neu"]
    compound_emo = emotions["compound"]
    main_DB(username, count, pos_emotion, neg_emotion, neu_emotion, compound_emo)
    #CURL LOGIC
    return(
    jsonify({
        "negative_sentiment" : neg_emotion,
        "positive_sentiment" : pos_emotion,
        "neutral_sentiment" : neu_emotion,
        "total_sentiment" : compound_emo,
        }))

@app.route("/tweetanalysis/", methods = ["GET"])
def main2():
    emotions = select_info()
    username = emotions["username"]
    pos_emotion = emotions["pos_emotion"]
    neg_emotion = emotions["neg_emotion"]
    neu_emotion = emotions["neu_emotion"]
    compound_emo = emotions["total_sentiment"]
    return(
    jsonify({
        "username": username,
        "negative_sentiment" : neg_emotion,
        "positive_sentiment" : pos_emotion,
        "neutral_sentiment" : neu_emotion,
        "total_sentiment" : compound_emo,
        }))

@app.route("/liked_tweet_analysis/", methods = ["POST"])
def main3():
    emotions = select_info()
    username = emotions["username"]
    pos_emotion = emotions["pos_emotion"]
    neg_emotion = emotions["neg_emotion"]
    neu_emotion = emotions["neu_emotion"]
    compound_emo = emotions["total_sentiment"]
    return(
    jsonify({
        "username": username,
        "negative_sentiment" : neg_emotion,
        "positive_sentiment" : pos_emotion,
        "neutral_sentiment" : neu_emotion,
        "total_sentiment" : compound_emo,
        }))

@app.route("/liked_tweet_analysis/", methods = ["GET"])
def main4():
    emotions = select_info()
    username = emotions["username"]
    pos_emotion = emotions["pos_emotion"]
    neg_emotion = emotions["neg_emotion"]
    neu_emotion = emotions["neu_emotion"]
    compound_emo = emotions["total_sentiment"]
    return(
    jsonify({
        "username": username,
        "negative_sentiment" : neg_emotion,
        "positive_sentiment" : pos_emotion,
        "neutral_sentiment" : neu_emotion,
        "total_sentiment" : compound_emo,
        }))

app.run(debug=True)
