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
    return [
        {"title": a["title"], "description": a["description"],
            "url": a["url"], "content": content}
        for a in news
        if (content := scrape_article(a["url"]))
    ]


def scrape_article(url: str):
    try:
        page = requests.get(url)
    except requests.exceptions.RequestException:
        return None
    if page.status_code != 200:
        return None
    soup = BeautifulSoup(page.text, 'html.parser')

    return " ".join(soup.get_text().split())
