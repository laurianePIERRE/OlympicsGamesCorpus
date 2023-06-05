from bs4 import BeautifulSoup as bs
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://iwf.sport/news-and-media/news/")
    soup=bs(page_source, "html.parser")
    items=soup.find_all("article", {"class":"post"})
    urls=[]
    names=[]
    for item in items:
        name= item.a['title']
        names.append(name)
        url= item.a["href"]
        urls.append(url)
    # pick other articles


    return urls, names

def pick_paragraph(url,file_output):
    """scrapp content  web page in a file and the plain code

       url : adress web page of federation internationnale of badminton
       file_output : file name created + file name plain

       return two files : file with htlm code and file with only text informations
       """
    page_source = usual_function.get_page_source(url)
    soup = bs(page_source, "html.parser")
    plain_soup = soup.encode("UTF-8")
    section = soup.find("section",{"class":"post-content"})
    paragraphs= section.find_all("div")
    result = ""
    for paragraphe in paragraphs:
        result = result + paragraphe.text + "\n"

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

