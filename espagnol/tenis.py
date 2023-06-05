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
    pages_url = ["http://www.ftm.es/noticias/generales/"]
    for page in pages_url :
        page_source = usual_function.get_page_source(page)
        soup=bs(page_source, "html.parser")
        section = soup.find("section", {"id":"page-body"})
        links = section.find_all("div", {"class": "detalle-listado"})
        for link in links:
            div_title = link.find ("h1", {"class":"listado-titulo"})
            if div_title:
                url_plain = div_title.a['href']
                url = "http://www.ftm.es"+url_plain
                urls.append(url)
                name = div_title.a.text
                name = re.sub(" ", "-", name)
                name = re.sub("[:\.\"\'/0-9?¿|]+", "", name)
                name = re.sub("Ó", "O", name)
                name = re.sub("á", 'a', name)
                name = re.sub("ó", 'o', name)
                name = re.sub("ñ", "n", name)
                names.append(name)

    return urls, names