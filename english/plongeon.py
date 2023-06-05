from bs4 import BeautifulSoup as bs
import requests
import re
import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.fina.org/news")

    soup=bs(page_source, "html.parser")
    section=soup.find("section", {"data-tags":"news,discipline:diving,discipline:highdiving"})
    articles = section.find_all("article")
    urls=[]
    names=[]

    for item in articles:
        sous_div=item.h3
        name= sous_div.text
        name = re.sub("\n", "", name)
        name = re.sub("[“”|]+", "", name)
        names.append(name)
        url= item.a["href"]
        url = "https://www.fina.org"+url
        urls.append(url)
        # pick other articles
    return urls, names
