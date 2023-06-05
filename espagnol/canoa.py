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
    urls_page= ["https://rfep.es/noticias-rfep/","https://rfep.es/noticias-rfep/page/2/"]
    for page in urls_page :
        page_source = usual_function.get_page_source(page)
        soup=bs(page_source, "html.parser")
        section = soup.find("div", {"class" :"itemList zn_blog_columns kl-blog--columns kl-cols"
                                             "-3 row isotope-initialized"})

        links= section.find_all("div", {"class":"itemHeader kl-blog-item-header"})

        for link in links:
            name = link.h3.a.text
            name = re.sub(" ", "-", name)
            name = re.sub("[:\./0-9?¿]+", "", name)
            name = re.sub("Ó", "O", name)
            names.append(name)
            url = link.h3.a['href']
            urls.append(url)
    return urls, names