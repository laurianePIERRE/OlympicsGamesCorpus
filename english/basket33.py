from bs4 import BeautifulSoup as bs
import usual_function
import requests
import re

def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://fiba3x3.com/en/news.html")
    soup=bs(page_source, 'html.parser')
    section = soup.find("div", {"class" : "news"})
    items=section.find_all("div", {"class":"news__item"})
    urls=[]
    names=[]
    for item in items:
        if len(urls)!=20:
            url_plain= item.a["href"]
            url = "https://fiba3x3.com"+url_plain
            urls.append(url)
            title_div = item.find("div", {"class":"news-list-item__content"})
            if title_div :
                name= title_div.h3.text
                names.append(name)



    return urls, names
