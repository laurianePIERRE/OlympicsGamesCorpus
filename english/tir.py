from bs4 import BeautifulSoup as bs
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.issf-sports.org/news_multimedia/newslist.ashx")
    soup=bs(page_source, "html.parser")
    section=soup.find("div", {"class":"row row-issfboxes"})
    articles = section.find_all("div", {"class" : "row row-issfboxes news"})
    urls=[]
    names=[]

    for article in articles:
        div = article.find("div", {"class":"col-md-7"})
        if div != None :
            name= div.a.h1.text
            names.append(name)
            url= div.a["href"]
            url = "https://www.issf-sports.org"+url
            urls.append(url)

    return urls, names
