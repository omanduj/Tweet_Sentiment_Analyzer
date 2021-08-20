import requests
import json
import yaml
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import os

def create_twitter_url(handle):
    """Purpose: To create correctly formatted twitter url
       Paramaters: handle, the username of the tweet account
       Return Value: url, a valid twitter user's url
    """
    max_results = 10
    mrf = "max_results={}".format(max_results)
    q = "query=from:{}".format(handle)
    url = "https://api.twitter.com/2/users/by/username/{}".format(handle)
    # url = "https://api.twitter.com/2/tweets/search/recent?{}&{}".format(mrf, q)
    return url

def get_bearer_token():
    """Purpose: To obtain bearer_token
       Paramaters: None
       Return Value: bearer_token to validate connection
    """
    bearer_token = os.environ.get("BEARER_TOKEN")
    #Done with exort BEARER_TOKEN=XXXXXXXX and import os
        #Gets bearer_token from environment variable
    return bearer_token
    
def auth_and_connect(bearer_token, url):
    """Purpose: Authorize and connect to twitter account. This is done via using a bearer token
                to access the given url
       Paramaters: bearer_token and url
       Return Value: response of the get request issued to twitter
    """
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    response = requests.request("GET", url, headers=headers)
    return response.json()

def seperating_tweets(data):
    """Purpose: To structure data returned from twitter
       Paramaters: data, information returned by twitter get request
       Return Value: username, the username of the account. user_id, the id associated with that account
    """
    user_id = data["id"]
    username = data["username"]
    return user_id, username

def getTweets(user_id, bearer_token, amount):
    """Purpose: To obtain tweets with the specified quieries
       Paramaters: user_id, bearer_token, amount
       Return Value: information returned from twitter
    """
    url = "https://api.twitter.com/2/users/{}/tweets".format(user_id)
    headers = {"Authorization": "Bearer {}".format(bearer_token)}

    params = {
              # "tweet.fields": "created_at",
              "end_time" : "2021-06-20T23:59:59.000Z",
              "start_time" : "2021-03-10T00:00:00.000Z",
              # "end_time" : "{}T23:59:59.000Z".format(end_at),
              # "start_time" : "{}T00:00:00.000Z".format(start_at),
              "max_results" : amount,
              }

    response = requests.request("GET", url, headers=headers, params=params)

    try:
        return(response.json()["data"])
    except KeyError:
        print(response.json())
        raise



def get_content(desired_tweets):
    """Purpose: To obtain tweets and restructure data
       Paramaters: desired_tweets, all tweets desired to go under analysis
       Return Value: list of tweets that has been cleaned
    """
    count = 0
    punctuation= '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    n = 2
    m = 2
    mod_string = ""
    mod_string2 = ""

    list_with_all_tweets = []
    for value in desired_tweets:
        list_with_all_tweets.append(desired_tweets[count]["text"])
        count = count + 1
    list_with_all_tweets = str(list_with_all_tweets).split(" ")

    for i in range(len(list_with_all_tweets[-1]) - n):
        mod_string = mod_string + list_with_all_tweets[-1][i]
    list_with_all_tweets[-1] = mod_string

    for i in range(len(list_with_all_tweets[0]) - m):
        i = i + m
        mod_string2 = mod_string2 + list_with_all_tweets[0][i]
    list_with_all_tweets[0] = mod_string2

    cleaned_list = []
    for word in list_with_all_tweets:
        myString = word
        newString = ""
        for letter in myString:
            if letter not in punctuation:
                newString = newString+letter
        word = newString
        cleaned_list.append(newString)

    return(cleaned_list)

def get_sentiment(finished_tweet_collection):
    """Purpose: obtain sentiment on given set of tweets
       Paramaters: finished_tweet_collection, all desired tweets
       Return Value: response, the final sentiment analysis
    """
    all_words_str = ""
    for value in finished_tweet_collection:
        all_words_str = all_words_str + value + " "
    # print(all_words_str, "\n")


    sentiment_analyzer = SentimentIntensityAnalyzer()
    final_analysis = sentiment_analyzer.polarity_scores(all_words_str)

    print(final_analysis)
    return final_analysis

def getTweets_liked_tweets(user_id, bearer_token, amount):
    """Purpose: obtain sentiment on given set of liked tweets
       Paramaters: user_id, bearer_token, amount
       Return Value: response, the final sentiment analysis
    """
    headers = {"Authorization": "Bearer {}".format(bearer_token)}

    response = requests.request("GET", "https://api.twitter.com/2/users/{}/liked_tweets?max_results={}".format(user_id, amount), headers=headers)
    return(response.json()["data"])

def main_API_one(url_handle, amount):
    """Purpose: To handle requests on the tweets end of the endpoint
       Paramaters: url_handle, amount
       Return Value: result of sentiment analyzer
    """
    # amount = input("Please enter amount of desired tweets (From 5-100): "  or "5")
    # handle = input("Please input handle of desired user: " or url_handle)

    # start_at = input("Please enter start date of desired tweets (format as YYYY-MM-DD): " )
    # end_at = input("Please enter end date of desired tweets (format as YYYY-MM-DD): " )
    url = create_twitter_url(url_handle)
    bearer_token = get_bearer_token()
    res_json = auth_and_connect(bearer_token, url)
    user_id, username = seperating_tweets(res_json["data"])
    desired_tweets = getTweets(user_id, bearer_token, amount)
    finished_tweet_collection = get_content(desired_tweets)
    return get_sentiment(finished_tweet_collection)

    # desired_tweets = getTweets(user_id, bearer_token, amount, start_at, end_at)
def main_API_two(url_handle, amount):
    """Purpose: To handle requests on the liked tweets end of the endpoint
       Paramaters: url_handle, amount
       Return Value: result of sentiment analyzer
    """
    # amount = input("Please enter amount of desired tweets (From 5-100): " or "5")
    # handle = input("Please input handle of desired user: " or "url_handle")
    # start_at = input("Please enter start date of desired tweets (format as YYYY-MM-DD): " )
    # end_at = input("Please enter end date of desired tweets (format as YYYY-MM-DD): " )
    url = create_twitter_url(url_handle)
    bearer_token = get_bearer_token()
    res_json = auth_and_connect(bearer_token, url)
    user_id, username = seperating_tweets(res_json["data"])
    liked_tweets = getTweets_liked_tweets(user_id, bearer_token, amount)
    finished_tweet_collection = get_content(liked_tweets)
    return get_sentiment(finished_tweet_collection)
