import sqlite3
import json



def base_set_up(username, num_of_tweets, pos_emotion, neg_emotion, neu_emotion, compound_emo):
    """Purpose: To set up database that will be used to save information returned by service
       Paramaters: A username, number of desired tweets, and the amount of each emotions
       Return Value: All the invormation in the database
    """
    conn = sqlite3.connect("sentiment_analysis_results.db")
    c = conn.cursor()

    # c.execute("""DROP TABLE IF EXISTS sentiment_results""")
    #
    # c.execute("""CREATE TABLE sentiment_results (
    #             id integer primary key autoincrement,
    #             username text,
    #             num_of_tweets integer,
    #             neg_emotion integer,
    #             neu_emotion integer,
    #             pos_emotion integer,
    #             compound_emo integer
    #          ) """)
    # conn.commit()

    c.execute("INSERT INTO sentiment_results (username, num_of_tweets, pos_emotion, neg_emotion, neu_emotion, compound_emo)VALUES (:username, :num_of_tweets, :pos_emotion, :neg_emotion, :neu_emotion, :compound_emo)",
                {"username": username, "num_of_tweets": num_of_tweets, "pos_emotion": pos_emotion,
                "neg_emotion": neg_emotion, "neu_emotion": neu_emotion, "compound_emo": compound_emo})
    c.execute("SELECT * FROM sentiment_results")

    information = c.fetchall()
    conn.commit()
    conn.close()
    return information

def select_info():
    """Purpose: To select data that user wants from database
       Paramaters: None
       Return Value: The requested information from the database in dictionary format
    """
    conn = sqlite3.connect("sentiment_analysis_results.db")
    c = conn.cursor()

    requested_info = c.execute("SELECT * FROM sentiment_results WHERE ID IS 20")

    requested_info = c.fetchall()
    requested_info = list(requested_info)

    cleaned_info = fix_data(requested_info)

    conn.commit()
    conn.close()
    return cleaned_info

def fix_data(information):
    """Purpose: To properly structure data for easiest use
       Paramaters: information, the data returned from the database
       Return Value: done_dictm, a dictionary with the data that is well structured
    """
    information = list(information[0])
    done_dict = {
                "username": information[1],
                "neg_emotion": information[3],
                "neu_emotion": information[4],
                "pos_emotion": information[5],
                "total_sentiment": information[6]
                }
    return done_dict

def main_DB(username, num_of_tweets, pos_emotion, neg_emotion, neu_emotion, compound_emo):
    information = base_set_up(username, num_of_tweets, pos_emotion, neg_emotion, neu_emotion, compound_emo)
    cleaned_info = fix_data(information)
    select_info()
    return cleaned_info
