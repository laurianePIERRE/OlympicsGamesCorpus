
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
    urls_pages = ["https://triatlon.org/fetri/noticias/",
                  "https://triatlon.org/fetri/noticias/?pagina=2"]
    for page in urls_pages:
        print(page)
        page_source = usual_function.get_page_source(page)

        soup = bs(page_source, "html.parser")
        section = soup.find("div", {"class": "row mt-4"})
        links = section.find_all("div", {"class":"col-sm-4"})
        for link in links:
            div_link = link.find("p", {"class": "mt-2 mb-2"})
            if div_link :
                url = div_link.a['href']
                urls.append(url)
                name = div_link.a.text
                name = re.sub(" ", "-", name)
                name = re.sub("[:\./0-9?¿,]+", "", name)
                name = re.sub("Ó", "O", name)
                name = re.sub('á','a',name)
                names.append(name)
    return urls, names
