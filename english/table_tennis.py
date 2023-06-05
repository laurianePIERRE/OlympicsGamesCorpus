from bs4 import BeautifulSoup as bs
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.ittf.com/news/")
    soup=bs(page_source, "html.parser")
    articles=soup.find_all("div", {"class":"col-xs-12 col-sm-6"})
    new_section = soup.find("div", {"class" : "row row-list-posts"})
    articles_add = new_section.find_all("div", {"class" : "col-xs-12"})
    urls=[]
    names=[]

    for article in articles:
        name= article.a["title"]
        names.append(name)
        url= article.a["href"]
        urls.append(url)

    for art in articles_add:

        name= art.a["title"]
        names.append(name)
        url= art.a["href"]
        urls.append(url)


            # pick other articles
    return urls, names
