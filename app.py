from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

# Load environment variables from key.env file
load_dotenv('key.env')

# Get the API key
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

app = Flask(__name__)

# Helper function to fetch news
def fetch_articles(query='India', page=1):
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}&page={page}&pagesize=10'
    response = requests.get(url)
    print(f"Fetching URL: {url}")  # Debugging line
    print(f"API Response Status Code: {response.status_code}")  # Debugging line
    print(f"API Response Content: {response.text}")  # Debugging line
    if response.status_code == 200:
        return response.json().get('articles', [])
    else:
        print(f"Error: {response.status_code}, {response.text}")  # Debug: Log errors
        return []

@app.route('/', methods=['GET'])
def index():
    query = request.args.get('query', 'India')  # Default to 'India' if not provided
    page = request.args.get('page', 1, type=int)  # Get the page number from the query parameters
    articles = fetch_articles(query, page)

    if not articles:
        error_message = "No articles available!"
        return render_template('index.html', articles=articles, error=error_message)

    return render_template('index.html', articles=articles,query=query,page=page)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/creator')
def creator():
    return render_template('creator.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)
