

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages():
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.fft.fr/actualites?q=actualites&page=1")
    soup=bs(page_source, "html.parser")
    page=soup.find("div",{"class":"view-content"})
    links= page.find_all("div", {"class" : "results-news-content"})
    urls=[]
    names=[]

    for link in links :
        sous_div = link.find("div",{"class":"views-field views-field-name title-videos-result-news"})

        if sous_div != None :
            url = sous_div.a['href']
            url = "https://www.fft.fr"+url
            urls.append(url)
            name = sous_div.a.text
            name = re.sub(" ","-",name)
            name = re.sub("[\xa0&;,#.\'\":\n\t]*","",name)
            names.append(name)
    return urls, names