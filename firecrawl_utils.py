from firecrawl import FirecrawlApp
import google.generativeai as genai
import os

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")
# Initialize Firecrawl SDK with API key
app = FirecrawlApp(api_key="fc-YOUR_API_KEY")


def scrape_website(url):
    """Scrape the given URL and return markdown and HTML content."""
    scrape_result = app.scrape_url(url, params={'formats': ['markdown', 'html']})
    response = model.generate_content("Analyze the webpage and extract the travel itinerary details, including dates, places, activities, and accommodations for the destination described. Identify the destination dynamically. After providing the itinerary, suggest bonus places to visit that are not mentioned in the main itinerary. Conclude with trivia or fun facts about the destination. Ensure no extra text is added. If the content is not an itinerary, respond with 'not a place, try again.'"+scrape_result['markdown'])
    return response.text

