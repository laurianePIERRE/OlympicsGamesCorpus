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
    pages_url = ["https://www.rfetm.es/noticias/categoria/2",
                "https://www.rfetm.es/noticias/categoria/2?page=2"]
    for page in pages_url :
        page_source = usual_function.get_page_source(page)
        soup=bs(page_source, "html.parser")
        section = soup.find("div", {"class":"container bg-white"})
        links = section.find_all("div", {"class": "col-12 col-xs-6 col-md-12 col-lg-12"
                                                  " col-xl-12 col-xxl-6 mb-2"})
        for link in links:
            div_title = link.find ("h6", {"class":"card-title mb-0 font-weight-bold"})
            if div_title:
                url= div_title.a['href']
                urls.append(url)
                name = div_title.a.text
                name = re.sub(" ", "-", name)
                name = re.sub("[:\.\"\'\n/0-9?¿|]+", "", name)
                name = re.sub("Ó", "O", name)
                name = re.sub("á", 'a', name)
                name = re.sub("ó", 'o', name)
                name = re.sub("ñ", "n", name)
                names.append(name)

    return urls, names