from bs4 import BeautifulSoup as bs
import requests
import re


def scrapp_article_content_OlympicDotCom(url, file_output):
    """scrapp content Olympics.com web page in a file and the plain code

    url : adress web page of olympics.com
    file_output : file name created + file name plain

    return two files : file with htlm code and file with only text informations
    """
    response = requests.get(url)
    html = response.content
    soup = bs(html, "lxml")
    plain_soup = soup.encode("UTF-8")
    section= soup.find_all("div", {"class": "wrapper"})
    for paragraphe in section :
        result = paragraphe.text

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


def scrapp_url_articles(url):
    """ scrapp articles' url from generic pages
        return list of urls  and lists names articles
    """
    pages_names = []
    urls = []
    response = requests.get(url)
    html = response.content
    soup = bs(html, "lxml")
    plain_soup = soup.encode("UTF-8")
    section = soup.find("section", {
        "class": "b2p-section -mosaic--5 -section--default b2p-grid__outer -no-y-gap"})
    sous_section = section.find_all("div", {"class": "card__image-container"})
    for lien in sous_section:
        url = lien.a['href']
        urls.append("https://olympics.com" + url)
        name = lien.a["data-analytics-link-tag"]
        pages_names.append(name)
    return urls, pages_names


def content_article(url, file_output):
    """scrapp content  web page in a file and the plain code

       url : adress web page of olympics.com
       file_output : file name created + file name plain

       return two files : file with htlm code and file with only text informations
       """
    response = requests.get(url)
    html = response.content
    soup = bs(html, "lxml")
    plain_soup = soup.encode("UTF-8")
    section = soup.find_all("section", {"class": "Gridstyles__GridContainer-sc-1p7u4tu-0 iQBUrm"
                                                 " slug__Wrapper-sc-1e9ul6f-0 hKZdKY"})

    for paragraphe in section:
        result = paragraphe.text

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

