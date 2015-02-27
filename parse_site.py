__author__ = 'NegatioN'

import requests
from bs4 import BeautifulSoup
import organize_info as oi
import regex_treatment as rt

#TODO Note, &Sort=2 is sorted decending by most seeders
#TODO note http://www.nyaa.se/?cats=1_37 is english translated anime  (make option to only have english-subbed anime)
#TODO write object oriented python? define class for "Torrent". use getEpisode() etc.

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
    for key, series_torrents in series_dictionary.items():
        if len(series_torrents) > 5:                        #says that only lists with more than 5 objects should actually
                                                        #be output to user.
            print(key)
            #print(str(series_urls[0]/1024) + " MiB" )
            for torrent in series_torrents:
                print(torrent.getName())




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

