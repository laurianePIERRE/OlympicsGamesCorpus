
from typing import Union, Any

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.rfea.es/noticias/comunicados.html")
    soup=bs(page_source, "html.parser")
    section=soup.find_all("tbody")[4]
    links = section.find_all("a")
    urls=[]
    names=[]

    for link in links:
        # limit to  20 links

       if len(names) != 20:
                url = link['href']
                url = "https://www.rfea.es/noticias/"+url
                urls.append(url)
                name= link.text
                name = re.sub(" ","-",name)
                name = re.sub(":","",name)
                names.append(name)
    return urls, names