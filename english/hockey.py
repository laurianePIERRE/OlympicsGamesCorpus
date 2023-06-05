from bs4 import BeautifulSoup as bs
import requests
import usual_function
import re

def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.fih.hockey/news")
    soup=bs(page_source, 'html.parser')
    section = soup.find_all("div", {"class" : "article-wrap"})
    urls=[]
    names=[]
    for lien in section:
        name = lien.find("div", {"class" : "article-content"}).h2.text
        names.append(name)
        url = lien.a["href"]
        urls.append(url)
    # pick other articles
    return urls, names