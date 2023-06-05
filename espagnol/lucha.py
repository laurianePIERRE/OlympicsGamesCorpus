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

    page_source = usual_function.get_page_source("https://www.felucha.com/blog/")
    soup=bs(page_source, "html.parser")
    section = soup.find("div", {"class": "post-list row"})
    links = section.find_all("div", {"class": "post-list-item col-xs-12 space-bottom "
                                              "col-sm-12 col-md-12"})
    for link in links:
        div_link = link.find("h2",{"class":"post-title text-left h3"})
        if div_link :
            url = div_link.a['href']
            urls.append(url)
            name = div_link.a.text
            name = re.sub(" ", "-", name)
            name = re.sub("[:\./0-9?¿|]+", "", name)
            name = re.sub("Ó", "O", name)
            name = re.sub("á",'a',name)
            name = re.sub("ó",'o',name)
            name = re.sub("ñ","n",name)
            names.append(name)

    return urls, names