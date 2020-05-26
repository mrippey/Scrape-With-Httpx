__author__ = "Michael Rippey @nahamike01"
__date__ = "2020/05/26"
"""
Author: Michael Rippey (c) 2020

Copyright 2020 Michael Rippey

See LICENSE.md for details
"""

import httpx 
from bs4 import BeautifulSoup
import urllib
import sys

def scrape_news_articles(site_name):
    news_links = []
    target_url = site_name

    try:
        make_request = httpx.get(target_url)

        soup = BeautifulSoup(make_request.content, 'html.parser')
        get_news_links = soup.find(class_="pickup-cat-wrap")

    except ConnectionError:
        sys.exit(1)

    for elements in get_news_links.find_all('a'):
        url = elements.get('href')
        linkd_info = urllib.parse.urljoin(target_url, url)
        news_links.append(linkd_info)
        print("[*]" + elements.text)
        
        


scrape_news_articles('https://cybersecurity-jp.com')