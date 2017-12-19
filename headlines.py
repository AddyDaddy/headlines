import feedparser
from flask import Flask, render_template

app = Flask(__name__)

RSS_FEED = {'bbc': "http://feeds.bbci.co.uk/news/world/rss.xml",
            'reuters': "http://feeds.reuters.com/Reuters/domesticNews",
            'cnn': "http://rss.cnn.com/rss/money_technology.rss",
            'fox': "http://feeds.foxnews.com/foxnews/latest"}

@app.route("/")
@app.route("/<publication>")
def get_news(publication="bbc"):
    feed = feedparser.parse(RSS_FEED[publication])
    first_article = feed['entries'][0]
    return render_template("home.html", articles=feed['entries'])


if __name__ == '__main__':
    app.run(port=5001, debug=True)
