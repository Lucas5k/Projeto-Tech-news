import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
    links = selector.css("div.cs-overlay a::attr(href)").getall()
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
    selector = Selector(text=html_content)

    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = "".join(
        selector.css("div.entry-header-inner h1.entry-title::text").getall()
    ).strip()
    timestamp = selector.css("div.entry-header-inner li.meta-date::text").get()
    writer = selector.css("div.entry-header-inner a.url::text").get()
    comments_count = len(
        selector.css("ol.comment-list div.comment-content::text").getall()
    )
    summary = "".join(
        selector.css("div.entry-content > p:nth-of-type(1) *::text").getall()
    ).strip()
    tags = selector.css("section.post-tags a[rel=tag]::text").getall()
    category = selector.css("div.meta-category span.label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""

    # pegar os links das primeiras N noticias do blog da trybe
    # fazer o scrap de cada noticia dos links que você pegou (req 4)
    # e retornar uma lista com todas as noticias no formato retornado pelo req 4

    my_list_of_news = []
    url_trybe = "https://blog.betrybe.com/"

    while len(my_list_of_news) < amount:
        request = fetch(url_trybe)
        new_news = scrape_novidades(request)

        for new in new_news:
            request_news = fetch(new)
            dict_of_news = scrape_noticia(request_news)
            my_list_of_news.append(dict_of_news)
        url_trybe = scrape_next_page_link(request)
    create_news(my_list_of_news[:amount])
    return my_list_of_news[:amount]
