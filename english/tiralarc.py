from bs4 import BeautifulSoup as bs
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.worldarchery.sport/news/latest")
    soup=bs(page_source, "html.parser")
    section=soup.find("ul", {"class":"row"})
    articles = section.find_all("article")
    urls=[]
    names=[]

    for article in articles:
        div = article.find("div", {"class":"article__field-short-title"})
        if div != None :
            name= div.a.text
            names.append(name)
            url= div.a["href"]
            url = "https://worldarchery.sport"
            urls.append(url)

    return urls, names
