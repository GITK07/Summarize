"""
from flask import Flask, render_template, request
import nltk
from newspaper import Article
import ssl

app = Flask(__name__)

ssl._create_default_https_context = ssl._create_unverified_context

nltk.download('punkt')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        url = request.form['url']
        article = Article(url)
        
        article.download()
        article.parse()

        article.nlp()

        title = article.title
        authors = ', '.join(article.authors) if article.authors else 'N/A'
        publish_date = article.publish_date if article.publish_date else 'N/A'
        summary = article.summary

        return render_template('result.html', title=title, authors=authors, publish_date=publish_date, summary=summary)
    except Exception as e:
        return f"An error occurred"

if __name__ == '__main__':
    app.run(debug=True)


"""

from flask import Flask, render_template, request
import nltk
from newspaper import Article
import ssl
import logging

# Create a Flask app
app = Flask(__name__)

# Ensure SSL context is created for downloading resources
ssl._create_default_https_context = ssl._create_unverified_context

# Download the required NLTK resource
nltk.download('punkt')

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        url = request.form['url']
        logger.info(f"Processing URL: {url}")
        article = Article(url)

        # Download and parse the article
        article.download()
        article.parse()

        # Check if article text is available
        if not article.text:
            logger.error("Article text not found")
            return "Article text not found. Please check the URL and try again."

        # Perform natural language processing
        article.nlp()

        title = article.title if article.title else 'N/A'
        authors = ', '.join(article.authors) if article.authors else 'N/A'
        publish_date = article.publish_date if article.publish_date else 'N/A'
        summary = article.summary if article.summary else 'No summary available.'

        logger.info("Summarization successful")
        return render_template('result.html', title=title, authors=authors, publish_date=publish_date, summary=summary)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return f"An error occurred"

if __name__ == '__main__':
    app.run(debug=True)

