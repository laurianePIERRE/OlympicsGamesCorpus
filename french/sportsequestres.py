

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    urls = []
    names = []
    urls_pages = ["https://www.ffe.com/actualites",
                 "https://www.ffe.com/actualites?page=1"]
    for page in urls_pages :
        page_source = usual_function.get_page_source(page)
        soup=bs(page_source, "html.parser")
        main_page = soup.find("ul", {"class":"grid"})
        links = main_page.find_all("h3", {"class" : "title"})
        for link in links :
            url = link.a['href']
            url = "https://www.ffe.com"+url
            urls.append(url)
            name = link.a.text
            name = re.sub(" ","-",name)
            name = re.sub("[\xa0&;,*:?\n\t]*","",name)
            names.append(name)
    return urls, names