import yfinance as yf
from newsapi import NewsApiClient
import datetime
import os

API_KEY = os.getenv("NEWS_API_KEY", "YOUR_NEWS_API_KEY")
if not API_KEY or API_KEY == "YOUR_NEWS_API_KEY":
    raise ValueError("Please set your News API key in the environment variable 'NEWS_API_KEY'.")

newsapi = NewsApiClient(api_key=API_KEY)

def fetch_financials(ticker='AAPL'):
    stock = yf.Ticker(ticker)
    info = stock.info
    return {
        "currentPrice": info.get("currentPrice"),
        "debtToEquity": info.get("debtToEquity"),
        "profitMargins": info.get("profitMargins"),
        "revenueGrowth": info.get("revenueGrowth")
    }

def fetch_news(company='Apple'):
    today = datetime.datetime.now().date()
    from_date = today - datetime.timedelta(days=7)
    articles = newsapi.get_everything(q=company,
                                      from_param=str(from_date),
                                      to=str(today),
                                      language='en',
                                      sort_by='relevancy',
                                      page_size=5)
    return [
        f"{a.get('title', '')} - {a.get('description', '')}"
        for a in articles["articles"]
    ]
# ...existing code...

if __name__ == "__main__":
    print(fetch_financials())
    print(fetch_news())