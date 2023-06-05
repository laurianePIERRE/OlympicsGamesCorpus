from bs4 import BeautifulSoup as bs
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source=usual_function.get_page_source("https://www.fifa.com/")
    soup=bs(page_source, "html.parser")
    section = soup.find("div", {"id" : "content"})
    items=section.find_all("div", {"data-asset":"article-card"})
    urls=[]
    names=[]
    for item in items:
        print ("boucle")
        print (item)
        name= item.find("p", {"class" : "ff-mb-16 ff-article-card_articleTitle__7nZbs ff-text-blue-cinema"}).text
        names.append(name)
        url= item.a["href"]
        url="https://www.fifa.com"+url
        urls.append(url)
    # pick other articles


    return urls, names

def content_article(url, file_output):
    """scrapp content  web page in a file and the plain code

       url : adress web page of federation internationnale of canoe

       file_output : file name created + file name plain

       return two files : file with htlm code and file with only text informations
       """
    response = requests.get(url)
    data= response.content
    soup = bs(data, features="html.parser")
    plain_soup = soup.encode("UTF-8")
    section = soup.find("div", {"class" : "container"})
    print (section)
    paragraphes = section.find_all("p")
    result=""
    for paragraphe in paragraphes:
        print ("paragraphe")
        print(paragraphe)
        result = result + paragraphe.text + "\n"
        print("result")
        print (result)
    url_file = file_output + ".txt"
    file = open(url_file, 'w', encoding="utf_8")
    file.write("infos provenant de" + url + "\n")
    file.write(result)
    file.close()
    url_plain_file = file_output + "_plain.txt"
    plain_file = open(url_plain_file, 'w')
    plain_file.write(str(plain_soup))
    plain_file.close()
    print("the file " + file_output + " has been created")

