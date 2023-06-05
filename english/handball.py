from bs4 import BeautifulSoup as bs
import requests
import usual_function
import re

def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.ihf.info/media-center/news")
    soup=bs(page_source, 'html.parser')
    section = soup.find_all("div", {"class" : "col-md-3 col-sm-6 col-xs-12"})
    urls=[]
    names=[]
    for lien in section:
        name = lien.find("div", {"class" : "cardText"}).h2.text
        names.append(name)
        url = lien.a["href"]
        url = "https://www.ihf.info"+url
        urls.append(url)
    # pick other articles
    return urls, names