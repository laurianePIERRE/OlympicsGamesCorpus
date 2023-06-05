from bs4 import BeautifulSoup as bs
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("http://worldskateboardingfederation.org/blog/")
    soup=bs(page_source, "html.parser")
    articles=soup.find_all("article")
    urls=[]
    names=[]

    for article in articles:
        if len(urls)!=20 :
          sous_div=article.find('div', {"class":"entry-thumbnail"})
          if sous_div != None :
              print (sous_div)
              name= sous_div.a["title"]
              names.append(name)
              url= sous_div.a["href"]
              urls.append(url)

            # pick other articles
    return urls, names
