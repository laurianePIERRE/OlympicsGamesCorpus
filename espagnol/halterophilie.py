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

    page_source = usual_function.get_page_source("https://www.fedehalter.org/noticias/")
    soup=bs(page_source, "html.parser")
    section = soup.find("div", {"class": "fusion-posts-container fusion-posts-container-"
                                       "pagination fusion-blog-rollover fusion-blog-layout"
                                       "-grid fusion-blog-layout-grid-4 isotope fusion-blog"
                                       "-equal-heights"})


    links = section.find_all("article")
    for link in links:
        div_link = link.find('div',{"class":"fusion-post-content-wrapper"})
        if div_link:
            url = link.h2.a['href']
            urls.append(url)
            name = div_link.h2.a.text
            name = re.sub(" ", "-", name)
            name = re.sub("[:\./0-9?¿|]+", "", name)
            name = re.sub("Ó", "O", name)
            name = re.sub("á",'a',name)
            name = re.sub("ó",'o',name)
            name = re.sub("ñ","n",name)
            names.append(name)

    return urls, names