__author__ = 'NegatioN'

import requests
from bs4 import BeautifulSoup
import organize_info as oi

#TODO Note, &Sort=2 is sorted decending by most seeders
#TODO note http://www.nyaa.se/?cats=1_37 is english translated anime  (make option to only have english-subbed anime)

#test method
def test(url, query):
    soup_list = getAllSoup(url, query)
    printAllPages(soup_list)

#test method
def printAllPages(soup_list):
    tuples = []
    while soup_list:
        oi.createTorrentTuples(soup_list.pop(), tuples)

    series_dictionary = oi.organizeTorrentsToSeries(tuples)
    for key, series_urls in series_dictionary.items():
        if len(series_urls) > 5:                        #says that only lists with more than 5 objects should actually
                                                        #be output to user.
            print(key)
            #print(str(series_urls[0]/1024) + " MiB" )
            for url in series_urls:
                print(url)




#creates a list of soup with all the pages with a torrent in them
def getAllSoup(url, query):
    #TODO query both these base-urls
    baseurl = "http://www.nyaa.se/?page=search&cats=1_37&filter=0&term="
    baseurl2 = "http://www.nyaa.se/?page=search&cats=1_38&filter=0&term="
    #replace space with + in the url for search
    query = query.replace(" ", "+")
    url = url + query

    url_list = [url]
    soup_list = []

    content = getContents(url) #init first search result.
    soup = BeautifulSoup(content.content)
    url_list = getPagesWithTorrents(soup, url_list)


    #adds soup as long as we have pages to take from
    #TODO thread-optimize requests
    while url_list:
        content = getContents(url_list.pop())
        soup_list.append(BeautifulSoup(content.content))

    return soup_list

#finds all the pages with torrents in them in the first page returned by search. //up to 29. putting down soft-limit.
#TODO implement get up to 100 pages? use rightpages and find limit there.
def getPagesWithTorrents(soup,url_list):
    pages = soup.findAll("div", {'class': 'pages'})
    page = pages[0]

    for a in page.findAll('a'):
        url_list.append(a['href'])

    return url_list

#gets the content of a page or returns an exception.
def getContents(url):
    try:
        cont = requests.get(url)
    except requests.exceptions.RequestException as e:
        raise SystemExit('\n' + str(e))
    return cont

