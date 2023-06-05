
from typing import Union, Any

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.feb.es/selecciones-3x3.aspx")
    soup=bs(page_source, "html.parser")
    links=soup.find_all("div", {"class":"nodo photo-landscape ar_1_5"})
    urls=[]
    names=[]
    print (links)

    for link in links:
        div_a = link.find("div",{"class":"titulo"})
        if div_a :

            url = div_a.a['href']
            print (url)
            urls.append(url)
            name= div_a.a['title']
            name = re.sub(" ","-",name)
            name = re.sub("[:\./0-9?¿]+","",name)
            name = re.sub("Ó","O",name)
            names.append(name)
    return urls, names

