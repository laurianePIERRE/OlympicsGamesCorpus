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
    page = "https://www.rfegolf.es/Noticias/NewsSection.aspx"
    page_source = usual_function.get_page_source(page)
    soup=bs(page_source, "html.parser")
    links= soup.find_all("div", {"class":"recuadro_noticia"})
    for link in links:
        div_title = link.find("div",{"id":"caja_titular"})
        if div_title :
            url_b =div_title.a['href']
            url = "https://www.rfegolf.es/"+url_b
            urls.append(url)
            name = div_title.a.text
            name = re.sub(" ", "-", name)
            name = re.sub("[:\./0-9?¿|]+", "", name)
            name = re.sub("Ó", "O", name)
            name = re.sub("á",'a',name)
            name = re.sub("ó",'o',name)
            names.append(name)

    return urls, names