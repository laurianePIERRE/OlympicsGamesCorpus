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
    urls_pages = ["https://www.iba.sport/news/",
                  "https://www.iba.sport/news/page/2/"]
    for page in urls_pages:
        page_source = usual_function.get_page_source(page)
        soup=bs(page_source, 'html.parser')
        section = soup.find("section", {"class" : "news__section"})
        items=section.find_all("div", {"class" : "photo"})
        for item in items:
            name= item.a["title"]
            names.append(name)
            url= item.a["href"]
            urls.append(url)

    return urls, names
