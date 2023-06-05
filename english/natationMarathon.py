from bs4 import BeautifulSoup as bs
import requests
import re
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = get_page_source("https://www.worldaquatics.com/news#swimming-news")

    soup=bs(page_source, "html.parser")
    section=soup.find("section", {"data-tags":"news,discipline:openwater"})
    links = section.find_all("li", {"class" : "content-list__item"})
    print ("links: ",len(links))
    urls=[]
    names=[]

    for link in links:
        name= link.a["title"]
        name = re.sub("\s {,2}" ," ",name)
        name = re.sub("\n", "", name)
        name = re.sub("[“”|]+", "", name)
        names.append(name)
        url= link.a["href"]
        url = "https://www.worldaquatics.com"+url
        urls.append(url)
        # pick other articles
    return urls, names

def get_page_source (url):
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        sleep(10)
        element = driver.find_element(By.XPATH,"//main/section[6]/button")
        driver.execute_script("arguments[0].click();", element)
        sleep(10)
        return driver.page_source
    finally:
        driver.quit()

