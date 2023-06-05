

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages():
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    urls=[]
    names=[]

    page_source = usual_function.get_page_source("https://www.ffvoile.fr/ffv/web/actualites/actus_liste.asp")
    soup=bs(page_source, "html.parser")
    section = soup.find("div", {"id" : "NewsList"})
    links= section.find_all("div", {"class" :"col-12 col-md-7 news-item"})


    for link in links :
        url = link.h4.a['href']
        url = "https://www.ffvoile.fr/ffv/web/actualites"+url
        urls.append(url)
        name = link.h4.a.text
        name = re.sub(" ","-",name)
        name = re.sub("[!?\xa0&;«»,#.\'\":\n\t|]*","",name)
        names.append(name)
    return urls, names