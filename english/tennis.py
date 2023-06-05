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
    urls_pages = ["https://www.itftennis.com/en/news-and-media/articles/?"]
    urls = []
    names = []
    for page in urls_pages :
        page_source = get_page_source(page)
        soup=bs(page_source, "html.parser")
        section=soup.find("div", {"class":"article-list-container container"})
        links = section.find_all("div", {"class" : "article-list__item-details-container"})
        for link in links:
            url = link.p.a["href"]
            url = "https://www.itftennis.com"+url
            urls.append(url)
            name= link.p.a.text
            name = re.sub("\s {,2}" ," ",name)
            name = re.sub(" ","-",name)
            name = re.sub("\n", "", name)
            name = re.sub("[“”\-|?]+", "", name)
            names.append(name)
    return urls, names

def get_page_source (url):
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        sleep(5)
        button_Cookies = driver.find_element(By.XPATH,"/html/body/div/div[3]/div/div[1]/div/div[2]/div/button[2]")
        driver.execute_script("arguments[0].click();", button_Cookies)
        sleep(10)
        button_Load_More = driver.find_element(By.XPATH,"/html/body/main/section/div/div[3]/div[3]/button")
        driver.execute_script("arguments[0].click();", button_Load_More)
        sleep(5)
        return driver.page_source
    finally:
        driver.quit()

