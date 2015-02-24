__author__ = 'NegatioN'

import requests
from bs4 import BeautifulSoup
import re

#TODO Note, &Sort=2 is sorted decending by most seeders
#TODO note http://www.nyaa.se/?cats=1_37 is english translated anime  (make option to only have english-subbed anime)


#returns a list of torrentpages with a title + info.
def createTorrentTuple(page_soup):
    #STRUCTURE = Tbody -> tr class tlistrow -> td
    table = page_soup.find_all("table", {'class': 'tlist'})
    #TODO get td class tlistname, tlistdownload, tlistsize, tlisticon -> a == http://www.nyaa.se/?cats=1_37  (english)
    #for td in page_soup.findAll('td'):
    for td in table:
        for tr in td.find_all("tr"): #each row
            for a in tr.find_all('a', {'href': 'http://www.nyaa.se/?cats=1_37'}): #for each tr in category "English subbed"
                for tlistname in tr.find_all("td", {'class': 'tlistname'}): #get something from this TR
                    print(tlistname)

            #print(a)


    return 0

def test(url, query):
    soup_list = getAllSoup(url, query)
    printAllPages(soup_list)

#test method
def printAllPages(soup_list):
    while soup_list:
        createTorrentTuple(soup_list.pop())


def organizeTorrentsToSeries(urls):
    series_dictionary = {} #dict holding all series -> torrents within series


    for url in urls:
        series_name = findSeriesName(url)
        if series_name not in series_dictionary:
            series_dictionary[series_name] = [] #create new list for given series in dictionary

        series_dictionary[series_name].append(url) #add url to the dictionary list for it's series

    return series_dictionary
    #Should sort all tuples into lists for their respective series.
    #Should throw away torrents with 0 seeders
    #Must have a method for defining what series it belongs to based on name of torrent.
        #Standard naming convention seems to be [subgroup] seriesname     episode etc
    #Should only keep torrents containing the given resolution. 720p 360p etc.
    #Should calculate total size of files in these torrents. (tlistsize) is field



#finds the name of a series based on the naming-convention [Subgroup] name - episode
def findSeriesName(url):
    string_array = re.split('(]|-)',url)
    return string_array[2].strip()  #for now index 2 should be the title. strip to remove trailing whitespace

#creates a list of soup with all the pages with a torrent in them
def getAllSoup(url, query):
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

#TODO Find proper use for method
def findName(link):
    #define name of the series.
    #TODO add link to replace here
    name=link.replace("http://www.animetake.com/anime/", "")
    name=name.replace("-", " ")
    name=name.replace("/", "")
    return name
