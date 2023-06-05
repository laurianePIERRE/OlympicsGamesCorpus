
from typing import Union, Any

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://breaking.ffdanse.fr/actualites/")
    soup=bs(page_source, "html.parser")
    page = soup.find("div", {"class":"elementor-jet-posts jet-elements"})
    liens = page.find_all("h4",{"class":"entry-title"})
    urls=[]
    names=[]

    for lien in liens :
        url = lien.a["href"]
        urls.append(url)
        name = lien.a.text
        name = re.sub("[:.\"\'\n/0-9?¿|,()]+", "", name)
        names.append(name)
    return urls,names
