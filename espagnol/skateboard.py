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
    pages_url = ["https://cnskateboarding.es/es/index.php",
                 "https://cnskateboarding.es/es/index.php?page=2"]
    for page in pages_url :
        page_source = usual_function.get_page_source(page)
        soup=bs(page_source, "html.parser")
        section = soup.find("div", {"class": "row"})
        links = soup.find_all("div", {"class": "col-md-4 col-sm-6 mb-4"})
        for link in links:
            plain_url = link.a['href']
            url = "https://cnskateboarding.es/es/"+plain_url
            urls.append(url)
            div_link = link.find("h5")
            if div_link :
                name = div_link.a.text
                name = re.sub(" ", "-", name)
                name = re.sub("[:\.\"\'/0-9?¿|]+", "", name)
                name = re.sub("Ó", "O", name)
                name = re.sub("á", 'a', name)
                name = re.sub("ó", 'o', name)
                name = re.sub("ñ", "n", name)
                names.append(name)

    return urls, names