In order for project to function, you must obtain and insert your own bearer_token
and export it to the OS

This project utilized the Twitter API along with the Flask framework to take in requests
and respond with a sentiment analyzer. It allows you to define the username and the amount
of recent tweets to analyze. The user is also able to decide whether they want the recent
tweets that have been tweeted or recent tweets that a user given has liked.

Example of viable request:
curl -X POST -H "Content-Type: application/json"
-d '{"username": "JoeBiden", "num_of_tweets": "5"}'
http://127.0.0.1:5000/liked_tweet_analysis/user
