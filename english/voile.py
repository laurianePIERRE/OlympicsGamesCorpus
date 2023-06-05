from typing import Union, Any

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.sailing.org/news/")
    soup=bs(page_source, "html.parser")
    section=soup.find("div", {"class":"aggregator__posts"})
    articles = section.find_all("article")
    urls=[]
    names=[]

    for article in articles:
        div = article.find("div", {"class":'news-card__content p-2'})

        if div != None :
            name=div.a['title']

            print (" name :", name)
            url=div.a['href']
            if re.match("/video/",url) is None:

                names.append(name)
                url = "https://www.sailing.org"+url
                urls.append(url)
    return urls,names