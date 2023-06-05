

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages():
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.fftt.com/site/mediatheque/revuepresse")
    soup=bs(page_source, "html.parser")
    links= soup.find_all("a", {"class" :"medias-index-large-item"})

    urls=[]
    names=[]

    for link in links :
        url = link['href']
        url = "https://www.ffft.com/"+url
        urls.append(url)
        name = link['title']
        name = re.sub(" ","-",name)
        name = re.sub("[!?\xa0&;«»,#.\'\":\n\t|]*","",name)
        names.append(name)
    return urls, names