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
    section=soup.find("section", {"data-tags":"news,discipline:artisticswimming"})
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
        if re.match("https://www.worldaquatics.com",url) :
            urls.append(url)
        else:
            url = "https://www.worldaquatics.com"+url
        # pick other articles
    return urls, names

def get_page_source (url):
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        sleep(5)
        button_accept_cookies = driver.find_element(By.XPATH,"//section[@id='js-cookie-notice']"
                                                             "/div/div/button[1]")
        driver.execute_script("arguments[0].click();",button_accept_cookies)
        sleep(5)
        element = driver.find_element(By.XPATH,"//main/section[5]/button")
        driver.execute_script("arguments[0].click();", element)
        sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        return driver.page_source
    finally:
        driver.quit()

