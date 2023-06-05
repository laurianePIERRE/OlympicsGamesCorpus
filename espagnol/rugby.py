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
    pages_url = ["https://ferugby.es/category/competiciones-internacionales",
                 "https://ferugby.es/category/competiciones-internacionales/page/2"]
    for page in pages_url :
        page_source = usual_function.get_page_source(page)
        soup=bs(page_source, "html.parser")
        section = soup.find("div", {"class": "td-ss-main-content"})
        links = section.find_all("div", {"class": "item-details"})
        for link in links:
            name = link.h3.a['title']
            name = re.sub(" ", "-", name)
            name = re.sub("[:\.\"\'/0-9?¿|]+", "", name)
            name = re.sub("Ó", "O", name)
            name = re.sub("á", 'a', name)
            name = re.sub("ó", 'o', name)
            name = re.sub("ñ", "n", name)
            names.append(name)
            url = link.h3.a['href']
            urls.append(url)
    return urls, names