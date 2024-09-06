from flask import Flask, render_template, request
from firecrawl_utils import scrape_website
import markdown
from serpapi import GoogleSearch

app = Flask(__name__)

def get_top_google_result(query):
    params = {
        "q": query,
        "api_key": "YOUR_API_KEY",
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    top_result = results['organic_results'][0]['link']  # Get the top result link
    return top_result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form.get('url')
    top_link = get_top_google_result("https://www.google.com/search?q=travel+itinerary+for+"+url)
    scrape_result = scrape_website(top_link)
    html_content = markdown.markdown(scrape_result)
    return render_template('index.html', url=url, result=html_content)

if __name__ == "__main__":
    app.run(debug=True)
