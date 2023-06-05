from bs4 import BeautifulSoup as bs
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://isasurf.org/news/")
    soup=bs(page_source, "html.parser")
    articles=soup.find_all("section")
    urls=[]
    names=[]

    for article in articles:
        print (article)
        sous_div = article.find("h4")
        if sous_div!=None:

            name= sous_div.a.text
            name = re.sub("\n","",name)
            name = re.sub("\t", " ", name)
            names.append(name)
            url= sous_div.a["href"]
            urls.append(url)

            # pick other articles
    return urls, names
