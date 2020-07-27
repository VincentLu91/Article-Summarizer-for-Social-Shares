from flask import Flask, render_template, request
from datetime import datetime
import validators
from article_extract import summarize_article_tr

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == "POST":
        article_link = request.form['article_link']
        if not article_link:
            error = 'Article Link is empty'
            return render_template('index.html', error=error)
        if not validators.url(article_link):
            error = 'Article Link is invalid'
            return render_template('index.html', error=error)
        summaries_tr = summarize_article_tr(article_link)
        if summaries_tr is None:
            error = 'Not enough summaries!'
            return render_template('index.html', error=error)
        return render_template('index.html', article_link=article_link, summaries_tr=summaries_tr)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)