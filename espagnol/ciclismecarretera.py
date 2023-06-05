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
    urls_page= ["https://rfec.com/index.php/es/smartweb/seccion/seccion/rfec/carretera/noticias_carretera",
                "https://rfec.com/index.php/es/smartweb/seccion/seccion/rfec/carretera/noticias_carretera/4",
                "https://rfec.com/index.php/es/smartweb/seccion/seccion/rfec/carretera/noticias_carretera/8",
                "https://rfec.com/index.php/es/smartweb/seccion/seccion/rfec/carretera/noticias_carretera/12"]
    for page in urls_page :
        page_source = usual_function.get_page_source(page)
        soup=bs(page_source, "html.parser")
        section = soup.find("ul", {"class" :"padding-left-0"})

        links= section.find_all("li")

        for link in links:
            div_link = link.find("h4")
            if div_link :

                name = div_link.text
                name = re.sub(" ", "-", name)
                name = re.sub("[:\./0-9?¿]+", "", name)
                name = re.sub("Ó", "O", name)
                names.append(name)
            url = link.a['href']
            urls.append(url)
    return urls, names