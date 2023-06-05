from typing import Union, Any

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function

def pick_adress_multi():
    all_urls=[]
    all_names=[]
    urls_gym = ["https://rfegimnasia.es/noticias/Especialidad/1",
                "https://rfegimnasia.es/noticias/Especialidad/2"]
    for url in urls_gym:
        urls_int, names_int = pick_adress_sport_pages(url)
        all_names = all_names + names_int
        all_urls = all_urls + urls_int
    return all_urls, all_names

def pick_adress_sport_pages(url_page) :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    urls = []
    names = []

    page_source = usual_function.get_page_source(url_page)
    soup=bs(page_source, "html.parser")
    section = soup.find("div", {"style": "margin-left:5px;margin-right:-10px;"})

    links= section.find_all("a")
    for link in links:

        if len(urls) != 11 :
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