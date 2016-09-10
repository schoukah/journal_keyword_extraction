from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()


def getLinks():
    global pages
    html = urlopen("http://ipe.sagepub.com/content/7/5.toc")
    bsObj = BeautifulSoup(html, "html.parser")
    try:
        entire = bsObj.findAll("a", {"rel":"abstract"}, href=re.compile("^(/content/)"))

    except AttributeError:
        print("This page is missing something! No worries though!")

    for link in entire:
        short = link.attrs['href']
        print(short)
        html1 = urlopen("http://ipe.sagepub.com"+short)
        bsObj2 = BeautifulSoup(html1, "html.parser")
        print(bsObj2.h1.get_text())
        keywords = bsObj2.findAll("a", {"class":"kwd-search"})
        for keyword in keywords:
            print(keyword.get_text())

getLinks()