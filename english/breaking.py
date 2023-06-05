from bs4 import BeautifulSoup as bs
import usual_function
import requests
import re

def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    urls = []
    names = []
    page_source = usual_function.get_page_source("https://www.breakingforgold.com/")
    soup=bs(page_source, 'html.parser')
    section = soup.find("div", {"class" : "col-sm-12 col-md-8"})
    items=section.find_all("div", {"class" : "article"})
    print("items :",items)
    for item in items:
        div_title = item.find("div", {"class":"articleContent"})
        if div_title :
            name= div_title.h2.a.text
            names.append(name)
            url= div_title.h2.a["href"]
            urls.append(url)

    return urls, names
