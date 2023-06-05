

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function

def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.ffpentathlon.fr/actualites/")
    soup=bs(page_source, "html.parser")
    page=soup.find("div", {"class":"container-flex flux-actus"})
    links = page.find_all("article")
    urls=[]
    names=[]

    for link in links :
        url = link.a['href']
        urls.append(url)
        div_name = link.find("h4", {"class":"bleu-clair"})
        if div_name :
            name = div_name.text
            name = re.sub(" ","-",name)
            name = re.sub("[,:.\"\n\t]*","",name)
            names.append(name)
    return urls, names
