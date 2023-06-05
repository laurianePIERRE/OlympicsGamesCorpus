from bs4 import BeautifulSoup as bs
import usual_function
import requests
import re

def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    urls = []
    names = []
    urls_pages = ["https://www.uci.org/news/bmx-freestyle/11VYzU6JcuNImiG4zBowoN?page=1",
                  "https://www.uci.org/news/bmx-freestyle/11VYzU6JcuNImiG4zBowoN?page=2"]
    for page in urls_pages:
        page_source = usual_function.get_page_source(page)
        soup=bs(page_source, 'html.parser')
        section = soup.find("ul", {"class" : "news-list__items"})
        items=section.find_all("div", {"class":"news-card__title"})

        for item in items:
            name = item.a.text
            names.append(name)
            url_plain = item.a["href"]
            url = "https://www.uci.org"+url_plain
            urls.append(url)
    return urls, names
