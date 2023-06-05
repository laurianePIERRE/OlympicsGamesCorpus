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
    pages_url = ["https://www.fesurf.es/blog/category/noticias/",
                 "https://www.fesurf.es/blog/category/noticias/page/2/"]
    for page in pages_url :
        page_source = usual_function.get_page_source(page)
        soup=bs(page_source, "html.parser")
        section = soup.find("div", {"class":"fusion-posts-container fusion-blog-layout-grid"
                                             " fusion-blog-layout-grid-2 isotope fusion-no-"
                                             "meta-info fusion-blog-equal-heights fusion-"
                                             "blog-pagination fusion-blog-rollover"})
        links = section.find_all("article")
        for link in links:
            url = link.h2.a['href']
            urls.append(url)
            name =link.h2.a.text
            name = re.sub(" ", "-", name)
            name = re.sub("[:\.\"\'/0-9?¿|]+", "", name)
            name = re.sub("Ó", "O", name)
            name = re.sub("á", 'a', name)
            name = re.sub("ó", 'o', name)
            name = re.sub("ñ", "n", name)
            names.append(name)

    return urls, names