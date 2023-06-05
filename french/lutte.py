

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages():
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.fflutte.com/actualites/?mode=list")

    soup=bs(page_source, "html.parser")
    page=soup.find("div", {"class":"post-list__items"})
    links = page.find_all("a")
    urls=[]
    names=[]
    for link in links:
        url = link["href"]
        urls.append(url)
        div_title = link.find("div", {"class":"item__content__title"})
        if div_title :
            name = div_title.text
            name = re.sub(" ","-",name)
            name = re.sub("[,:\n\t]*","",name)
            names.append(name)
    return urls,names