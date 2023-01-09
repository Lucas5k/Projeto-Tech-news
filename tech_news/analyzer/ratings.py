from tech_news.database import find_news


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    all_news = find_news()
    numbers = [number["comments_count"] for number in all_news]
    min_number = list(set(numbers))
    min_number.pop(0)
    print(min_number)
    my_list_of_tuples = [
        (new["title"], new["url"])
        for new in all_news
        if new["comments_count"] <= min_number[1]
    ]
    print(my_list_of_tuples)
    return my_list_of_tuples


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
