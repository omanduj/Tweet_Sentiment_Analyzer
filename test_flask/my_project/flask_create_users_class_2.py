from flask import Flask, url_for, render_template, request, jsonify
from markupsafe import escape, Markup
import yaml
from test_flask.my_project.pythonAPY_ import main_API_one, create_twitter_url, main_API_two



app = Flask(__name__)

@app.route("/tweetanalysis/<string:user_name>", methods = ["POST"])
#CURL STUFF
def main(user_name):
    some_json = request.get_json()
    username = some_json["username"]
    count = some_json["num_of_tweets"]
    emotions = main_API_one(username, count)
    pos_emotion = emotions["pos"]
    neg_emotion = emotions["neg"]
    neu_emotion = emotions["neu"]
    compound_emo = emotions["compound"]
    #CURL LOGIC
    return(
    jsonify({
        "negative_sentiment" : neg_emotion,
        "positive_sentiment" : pos_emotion,
        "neutral_sentiment" : neu_emotion,
        "total_sentiment" : compound_emo,
        }))

# @app.route("/tweetanalysis/<string:user_name>", methods = ["GET"])
# def main2(user_name):
#     emotions = main_API_one(user_name)
#     pos_emotion = emotions["pos"]
#     neg_emotion = emotions["neg"]
#     neu_emotion = emotions["neu"]
#     compound_emo = emotions["compound"]
#     return(
#     jsonify({
#         "negative_sentiment" : neg_emotion,
#         "positive_sentiment" : pos_emotion,
#         "neutral_sentiment" : neu_emotion,
#         "total_sentiment" : compound_emo,
#         }))


@app.route("/liked_tweet_analysis/<string:user_name>", methods = ["POST"])
def main3(user_name):
    some_json = request.get_json()
    username = some_json["username"]
    count = some_json["num_of_tweets"]
    emotions = main_API_two(username, count)
    pos_emotion = emotions["pos"]
    neg_emotion = emotions["neg"]
    neu_emotion = emotions["neu"]
    compound_emo = emotions["compound"]
    #CURL LOGIC
    return(
    jsonify({
        "negative_sentiment" : neg_emotion,
        "positive_sentiment" : pos_emotion,
        "neutral_sentiment" : neu_emotion,
        "total_sentiment" : compound_emo,
        }))

# @app.route("/liked_tweet_analysis/<string:user_name>", methods = ["GET"])
# def main4(user_name):
#     emotions = main_API_two(user_name)
#     pos_emotion = emotions["pos"]
#     neg_emotion = emotions["neg"]
#     neu_emotion = emotions["neu"]
#     compound_emo = emotions["compound"]
#     return(
#     jsonify({
#         "negative_sentiment" : neg_emotion,
#         "positive_sentiment" : pos_emotion,
#         "neutral_sentiment" : neu_emotion,
#         "total_sentiment" : compound_emo,
#         }))

app.run(debug=True)
