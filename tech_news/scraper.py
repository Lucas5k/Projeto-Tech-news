import requests
import time
from parsel import Selector


headers = {"user-agent": "Fake user-agent"}


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, headers=headers, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    links = selector.css('div.cs-overlay a::attr(href)').getall()
    if not links:
        return []
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    next_page = selector.css("div.nav-links > a.next::attr(href)").get()
    return next_page


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
