

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
    urls_page = ["https://www.ffjudo.com/actualites",
                 "https://www.ffjudo.com/actualites/2",
                 "https://www.ffjudo.com/actualites/3"]
    for page in urls_page:
        page_source = usual_function.get_page_source(page)

        soup=bs(page_source, "html.parser")
        page=soup.find("div", {"class":"listing__actu--list"})
        links = page.find_all("div", {"class":"listing__actu--item"})

        for link in links:
            url =link.a['href']
            urls.append(url)
            name = link.h2.text
            name = re.sub(" ","-",name)
            name = re.sub("[,:\n\t]*","",name)
            names.append(name)
    return urls,names