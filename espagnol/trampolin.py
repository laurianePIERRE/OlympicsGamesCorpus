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

    page_source = usual_function.get_page_source("https://rfegimnasia.es/noticias/Especialidad/4")
    soup=bs(page_source, "html.parser")
    section = soup.find("div", {"style": "margin-left:5px;margin-right:-10px;"})

    links= section.find_all("a")
    for link in links:

        if len(urls) != 20 :
            url_b = link['href']
            url = "https://rfegimnasia.es/" + url_b
            urls.append(url)
            div_title = link.find("div",{"class":"col-sm-3"})
            if div_title :
                name = div_title.text
                name = re.sub(" ", "-", name)
                name = re.sub("[:\./0-9?¿|]+", "", name)
                name = re.sub("Ó", "O", name)
                name = re.sub("á",'a',name)
                name = re.sub("ó",'o',name)
                names.append(name)

    return urls, names