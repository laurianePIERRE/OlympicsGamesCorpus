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

    page_source = usual_function.get_page_source("https://www.rfeh.es/archivo-noticias/")
    soup=bs(page_source, "html.parser")
    section = soup.find("div", {"class": "main-loop-inner"})
    links = section.find_all("div", {"class":"panel"})
    for link in links:
        div_link = link.find("div",{"class":"article-excerpt"})
        if div_link :
            url = link.h2.a['href']
            urls.append(url)
            name = link.h2.a.text
            name = re.sub(" ", "-", name)
            name = re.sub("[:\./0-9?¿|]+", "", name)
            name = re.sub("Ó", "O", name)
            name = re.sub("á",'a',name)
            name = re.sub("ó",'o',name)
            name = re.sub("ñ","n",name)
            names.append(name)

    return urls, names