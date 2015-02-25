__author__ = 'NegatioN'

import requests
from bs4 import BeautifulSoup
import re

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
        createTorrentTuples(soup_list.pop(), tuples)

    series_dictionary = organizeTorrentsToSeries(tuples)
    for key, series_urls in series_dictionary.items():
        if len(series_urls) > 5:
            print(key)
            print(str(series_urls[0]/1024) + " MiB" )
            for url in series_urls:
                print(url)

#takes in the soup of a single page, a list to append tuples to
#returns a list of all torrents that match search with url, name, size(in kb)
def createTorrentTuples(page_soup, tuples):
    #STRUCTURE = Tbody -> tr class tlistrow -> td
    table = page_soup.find_all("table", {'class': 'tlist'})

    #TODO get td class tlistname, tlistdownload, tlistsize, tlisticon -> a == http://www.nyaa.se/?cats=1_37  (english)
    #for td in page_soup.findAll('td'):
    for td in table:
        for tr in td.find_all("tr"): #each row
            for a in tr.find_all('a', {'href': 'http://www.nyaa.se/?cats=1_37'}): #for each tr in category "English subbed"
                tuples.append(createTuple(tr))
                #TODO keep the TR in array of soup-objects? Iterate upon these later?
                #for current purposes we need url, size, determine what series it belongs to. way to sort out duplicates
                #and only of a spesific resolution.


    return tuples

#returns a tuple with download_url, torrent_name, torrent_size
#takes in a soup-object's TR-row.
def createTuple(tr_soup):
    download_url = tr_soup.find('td', {'class':'tlistdownload'}).a['href']  #gets link to download torrent directly
    torrent_name = tr_soup.find('td', {'class':'tlistname'}).a.contents[0]  #gets name of torrent
    size_text = tr_soup.find('td', {'class':'tlistsize'}).contents[0]
    torrent_size = getTorrentSize(size_text)                                #computes the size of the torrent in kilobytes

    torrent_tuple = (download_url, torrent_name, torrent_size)                #compounds all fields into tuple

    return torrent_tuple

#should take in a tuple with download_url, torrent_name, torrent_size
def organizeTorrentsToSeries(torrent_tuples):
    series_dictionary = {} #dict holding all series -> torrents within series


    for torrent_url,torrent_name,torrent_size in torrent_tuples:
        series_name = findSeriesName(torrent_name)                  #get name of series from torrent_name
        if isCorrectResolution(torrent_name,720):

            if series_name not in series_dictionary:
                #create new list for given series in dictionary
                series_dictionary[series_name] = [torrent_size]     #size is always available at index 0
            else:
                series_dictionary[series_name][0] += torrent_size   #size is always available at index 0
            series_dictionary[series_name].append(torrent_url)     #add url to the dictionary list for it's series

    return series_dictionary
    #Should sort all tuples into lists for their respective series.
    #Should throw away torrents with 0 seeders
    #Must have a method for defining what series it belongs to based on name of torrent.
        #Standard naming convention seems to be [subgroup] seriesname     episode etc
    #Should only keep torrents containing the given resolution. 720p 360p etc.
    #Should calculate total size of files in these torrents. (tlistsize) is field

#determines if the current torrent_name tested has the resolution we want
def isCorrectResolution(torrent_name, resolution):  #takes string, int
    resolution = str(resolution) + 'p'  #example 720 becomes 720p
    regex = re.compile(resolution)
    if regex.search(torrent_name) is not None:
        return True
    else:
        return False

#example: 258.3 MB, 13.7 GB, 200 KB
#returns size as int in KB size
def getTorrentSize(size_string):
    if size_string == "":
        return 0
    size_string = size_string.lower() #convert to lowercase for easier matching
    size = float(re.split('\s',size_string)[0]) #should leave size as the first index of array returned
    kb = "kib"
    mb = "mib"
    gb = "gib"
    regex = re.compile(kb)
    if regex.search(size_string) is not None:
        return size
    regex = re.compile(mb)
    if regex.search(size_string) is not None:
        return size*1024
    regex = re.compile(gb)
    if regex.search(size_string) is not None:
        return size*1024*1024
    #if no match, assume size is less than one kb and return 1
    return 1


#finds the name of a series based on the naming-convention [Subgroup] name - episode
def findSeriesName(url):
    string_array = re.split('(]|-)',url)
    if len(string_array) > 2:
        return string_array[2].strip()  #for now index 2 should be the title. strip to remove trailing whitespace
    else:
        return url

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
