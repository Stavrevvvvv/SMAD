# backend/app.py
from flask import Flask, jsonify
from utils.twitter_api import get_tweets
from utils.sentiment import analyze_sentiment

app = Flask(__name__)

@app.route('/analyze/<keyword>')
def analyze_keyword(keyword):
    tweets = get_tweets(keyword)
    results = [{"tweet": tweet["text"], "sentiment": analyze_sentiment(tweet["text"])} for tweet in tweets]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
