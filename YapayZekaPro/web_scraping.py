import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

"""

def fetch_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch page {response.status_code}")
        return None

def parse_html(html):
    soup = BeautifulSoup(html,"html.parser")
    return soup

def get_stock_price(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}"
    html = fetch_page(url)
    if not html:
        return None
    soup = parse_html(html)
    price_tag = soup.find("fin-streamer", {"data-symbol": ticker,"data-field":"regularMarketPrice"})
    if price_tag:
        return price_tag.text
    else:
        print("Stock price not found")
        return None
def track_stock_price(ticker,interval=60):  ###her iki saniyede bir fiyat çeker gibi
    while True:
        price = get_stock_price(ticker)
        if price:
            print(f"{ticker}: {price}")
        time.sleep(interval)

ticker = "FUN"
track_stock_price(ticker,2)
"""

def fetch_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch page {response.status_code}")

def parse_html(html):
    soup = BeautifulSoup(html,"html.parser")
    return soup

def get_stock_price(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}"
    html = fetch_page(url)
    if not html:
        return None
    soup = parse_html(html)
    price_tag = soup.find("fin-streamer", {"data-symbol": ticker,"data-field":"regularMarketPrice"})
    if price_tag:
        return price_tag.text
    else:
        print("Stock price not found.")
        return None

def track_stock_price(ticker,interval=60):
    while True:
        price = get_stock_price(ticker)
        if price:
            print(f"{ticker}:${price}")
        time.sleep(interval)
def main():
    ticker = input("Enter the stock ticker symbol: ").upper()
    interval = int(input("Enter the update interval in seconds : "))
    print(f"Trcking stock prices for {ticker} every {interval} secondsss..")
    track_stock_price(ticker,interval)

if __name__ == '__main__':
    main()



