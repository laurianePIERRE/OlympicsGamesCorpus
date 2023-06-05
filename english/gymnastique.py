from bs4 import BeautifulSoup as bs
import requests

import usual_function

from bs4 import BeautifulSoup as bs
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    men_page_source = usual_function.get_page_source("https://www.gymnastics.sport/site/"
                                                     "discipline.php?disc=2")
    men_soup=bs(men_page_source, "html.parser")
    men_section=men_soup.find("div", {"id":"sportnews"})
    # we must  select the urls on two loop ( men and women categories)

    all_urls = []
    all_names = []
    men_articles = men_section.find_all("div", {"class" : "news-teaser news-teaser--smaller"})
    men_urls=[]
    men_names=[]

    for article in men_articles:
        url = article.a['href']
        url = re.sub("./","/",url)
        url = re.sub("/new/","/news/",url)
        url = "https://www.gymnastics.sport/site"+url
        men_urls.append(url)
        div = article.find ("div", {"class":"news-teaser__body"})
        if div != None :
            name = div.h3.text
            men_names.append(name)

    # the same for the women
    women_page_source = usual_function.get_page_source("https://www.gymnastics.sport/site/"
                                                       "discipline.php?disc=3")
    women_soup = bs(women_page_source, 'html.parser')
    women_section = women_soup.find('div', {"id":"sportnews"})
    women_articles = women_section.find_all("div", {"class" : "news-teaser news-teaser--smaller"})
    women_urls=[]
    women_names=[]

    for article in women_articles:
        url = article.a['href']
        url = re.sub("./","/",url)
        url = re.sub("/new/","/news/",url)
        url = "https://www.gymnastics.sport/site"+url
        women_urls.append(url)
        div = article.find ("div", {"class":"news-teaser__body"})
        if div != None :
            name = div.h3.text
            women_names.append(name)

    all_urls = men_urls + women_urls
    all_names = men_names + women_names
    return all_urls,all_names