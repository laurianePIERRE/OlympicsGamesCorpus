
from typing import Union, Any

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages():
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    urls = []
    names = []
    urls_pages = ["https://rfev.es/default/actualidad/index/all/1",
                  "https://rfev.es/default/actualidad/index/page/2/all/1",
                  "https://rfev.es/default/actualidad/index/page/3/all/1",
                  "https://rfev.es/default/actualidad/index/page/4/all/1"]
    for page in urls_pages:
        page_source = usual_function.get_page_source(page)
        soup = bs(page_source, "html.parser")
        section = soup.find("div", {"id":"container"})
        links = section.find_all("h3", {"class":"listtitle"})
        for link in links:
            url_plain = link.a['href']
            url = "https://rfev.es"+url_plain
            urls.append(url)
            name = link.a.text
            name = re.sub(" ", "-", name)
            name = re.sub("[:\./0-9?¿,]+", "", name)
            name = re.sub("Ó", "O", name)
            name = re.sub('á','a',name)
            names.append(name)
    return urls, names
