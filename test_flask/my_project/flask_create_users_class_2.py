from flask import Flask, url_for, render_template, request, jsonify
from markupsafe import escape, Markup
import yaml
from test_flask.my_project.pythonAPY_ import main_API_one, create_twitter_url, main_API_two



app = Flask(__name__)

@app.route("/tweetanalysis/<string:user_name>", methods = ["POST"])
def main(user_name):
    some_json = request.get_json()
    # print(create_twitter_url())
    return(
    jsonify({
        "Info sent is " : some_json
        }))

@app.route("/tweetanalysis/<string:user_name>", methods = ["GET"])
def main2(user_name):
    emotions = main_API_one(user_name)
    pos_emotion = emotions["pos"]
    neg_emotion = emotions["neg"]
    neu_emotion = emotions["neu"]
    compound_emo = emotions["compound"]
    return(
    jsonify({
        "negative_sentiment" : neg_emotion,
        "positive_sentiment" : pos_emotion,
        "neutral_sentiment" : neu_emotion,
        "total_sentiment" : compound_emo,
        }))


@app.route("/liked_tweet_analysis/<string:user_name>", methods = ["POST"])
def main3(user_name):
    return(
    jsonify({
        "user_name" : "barackObama",
        "end_time" : "2021-06-20T23:59:59.000Z",
        "start_time" : "2021-03-10T00:00:00.000Z",
        "num_of_tweets" : "10",
        }))

@app.route("/liked_tweet_analysis/<string:user_name>", methods = ["GET"])
def main4(user_name):
    emotions = main_API_two(user_name)
    pos_emotion = emotions["pos"]
    neg_emotion = emotions["neg"]
    neu_emotion = emotions["neu"]
    compound_emo = emotions["compound"]
    return(
    jsonify({
        "negative_sentiment" : neg_emotion,
        "positive_sentiment" : pos_emotion,
        "neutral_sentiment" : neu_emotion,
        "total_sentiment" : compound_emo,
        }))

app.run(debug=True)
