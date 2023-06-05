from typing import Union, Any

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function

def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    urls = []
    names = []
    pages_url = ["https://rfen.es/es/posts/news?discipline=98",
                 "https://rfen.es/es/posts/news?page=2&discipline=98",
                 "https://rfen.es/es/posts/news?page=3&discipline=98",
                 "https://rfen.es/es/posts/news?page=4&discipline=98"]
    for page in pages_url :
        page_source = usual_function.get_page_source(page)
        soup=bs(page_source, "html.parser")
        section = soup.find("div", {"class": "posts-container"})
        links = section.find_all("div", {"class": "box-info post-container"})
        for link in links:
            name = link.h2.text
            name = re.sub(" ", "-", name)
            name = re.sub("[:\.\"\'/0-9?¿|]+", "", name)
            name = re.sub("Ó", "O", name)
            name = re.sub("á", 'a', name)
            name = re.sub("ó", 'o', name)
            name = re.sub("ñ", "n", name)
            names.append(name)
            div_link = link.find("a", {"class": "absolute"})
            if div_link :
                url = div_link['href']
                urls.append(url)
    return urls, names