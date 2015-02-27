__author__ = 'NegatioN'

import requests
from bs4 import BeautifulSoup
import organize_info as oi
import regex_treatment as rt

#TODO always get trusted torrents first, where no duplicates. Blue rows. class="aplus tlistrow"

#test method
def test(url, query):
    soup_list = getAllSoup(url, query)
    printAllPages(soup_list)

#test method
def printAllPages(soup_list):
    torrents = []
    while soup_list:
        oi.createTorrentList(soup_list.pop(), torrents)

    series_dictionary = oi.organizeTorrentsToSeries(torrents)
    outputInformation(series_dictionary)


def outputInformation(series_dictionary):
    for key, series_torrents in series_dictionary.items():
        if len(series_torrents) > 5:                  #says that only lists with more than 5 objects should be output
            totalSize = 0
            for torrent in series_torrents:
                totalSize += torrent.getSize()
            totalSize = totalSize/1024/1024   #outbout gb
            sizeString = "{0:.2f}".format(totalSize)            #format with two decimals
            print(key + " - " + str(len(series_torrents)) + " episodes - " + sizeString + " GiB")




#creates a list of soup with all the pages with a torrent in them
def getAllSoup(url, query):
    #TODO query both these base-urls
    #replace space with + in the url for search
    query = query.replace(" ", "+")
    url_with_query = url + query

    url_list = [url]
    soup_list = []

    content = getContents(url_with_query) #init first search result.
    soup = BeautifulSoup(content.content)
    url_list = getPagesWithTorrents(soup, url_with_query)
    print(url_list)


    #adds soup as long as we have pages to take from
    #TODO thread-optimize requests
    while url_list:
        content = getContents(url_list.pop())
        soup_list.append(BeautifulSoup(content.content))

    return soup_list

#finds all the pages with torrents in them in the first page returned by search. //up to 29. putting down soft-limit.
def getPagesWithTorrents(soup,url_with_query):

    url_list = createUrlList(url_with_query, extractLastPageNumber(soup))

    return url_list

#gets the content of a page or returns an exception.
def getContents(url):
    try:
        cont = requests.get(url)
    except requests.exceptions.RequestException as e:
        raise SystemExit('\n' + str(e))
    return cont

#TODO implement producer/consumer threads
def extractLastPageNumber(soup):
    #should get from div class rightpages  (2 instances)
    # anchor class "page pagelink", last instance get

    rightpages = soup.findAll("div", {'class': 'rightpages'})
    pageUrls = []
    for a in rightpages[0].findAll('a'):
        pageUrls.append(a['href'])

    return rt.getPageNumber(pageUrls.pop())

def createUrlList(baseurl_with_query, limit_page_num):
    i = 1
    offset_text = "&offset="
    urls = []
    while i < limit_page_num+1:
        url = baseurl_with_query + offset_text + str(i)
        urls.append(url)
        i+=1
    return urls

