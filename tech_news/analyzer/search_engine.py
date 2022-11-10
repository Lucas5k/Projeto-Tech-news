from tech_news.database import search_news, find_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    my_tuple = tuple()
    my_list_of_tuples = []
    list_of_titles = search_news({"title": {"$regex": title, "$options": "i"}})
    for titles in list_of_titles:
        title = titles["title"]
        url = titles["url"]
        my_tuple = (title, url)
        my_list_of_tuples.append(my_tuple)
    return my_list_of_tuples


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
