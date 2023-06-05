

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages():
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.fftir.org/menu/actualite/")
    soup=bs(page_source, "html.parser")
    page=soup.find("div", {"id":"content"})
    print (page.prettify())
    links= page.find_all("div", {"class":"media"})
    urls=[]
    names=[]

    for link in links :
        print ("link in loop :")
        print(link)
        url = link.a['href']
        urls.append(url)
        name = link.a.text
        name = re.sub(" ","-",name)
        name = re.sub("[!?\xa0&;,#.\'\":\n\t|]*","",name)
        names.append(name)
    return urls, names