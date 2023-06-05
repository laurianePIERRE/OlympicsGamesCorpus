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
    page = "https://fedme.es/categoria/escalada/"
    page_source = usual_function.get_page_source(page)
    soup=bs(page_source, "html.parser")
    section = soup.find("div", {"class" :"posts_container"})
    links= section.find_all("article")
    for link in links:
        div_link = link.find("h2")
        if div_link :
            name = div_link.a.text
            name = re.sub(" ", "-", name)
            name = re.sub("[:\./0-9?¿]+", "", name)
            name = re.sub("Ó", "O", name)
            names.append(name)
            url = link.a['href']
            urls.append(url)
    return urls, names