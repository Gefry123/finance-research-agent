from dotenv import load_dotenv
import os
from newsapi import NewsApiClient
from bs4 import BeautifulSoup
import requests

load_dotenv()
news_api_key = os.getenv("NEWS_API_KEY")

newsapi = NewsApiClient(api_key=news_api_key)


def fetch_news(ticker: str):
    return format_headlines(newsapi.get_everything(q=ticker)["articles"][:10])


def format_headlines(news: list):
    return [{"title": a["title"], "description": a["description"], "url": a["url"]} for a in news]


def scrape_article(url: str):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup.get_text()
