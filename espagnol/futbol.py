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
    urls_pages = ["https://www.rffm.es/futbol/futbol-base",
                 "https://www.rffm.es/futbol/futbol-base?page=2" ]
    for page in urls_pages:
        page_source = usual_function.get_page_source(page)
        soup=bs(page_source, "html.parser")
        links= soup.find_all("div", {"class":"post-preview medium"})
        for link in links:
            div_title = link.find("a", {"class": "post-preview-title"})
            if div_title:
                url = div_title['href']
                urls.append(url)
                name = div_title.text
                name = re.sub(" ", "-", name)
                name = re.sub("[:\.\n/0-9?¿|]+", "", name)
                name = re.sub("Ó", "O", name)
                name = re.sub("á",'a',name)
                name = re.sub("ó",'o',name)
                names.append(name)

    return urls, names