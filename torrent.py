__author__ = 'NegatioN'

import re

#TODO implement is_movie field, regex torrent for movie etc.
#TODO let be is_series if "Season x" regex match?

#this class represents a torrent, and contains all the information we want to track about it.
#constructor currently takes in a tr_soup from beautifulsoup4
class Torrent:
    is_series = False
    is_aplus = False    #manually verified torrents by nyaa.se that is optimal quality.
    episode_number = 0
    url = ""
    name = ""
    size = 0
    seeders = 0

    #takes in a tr_soup from nyaa.se
    def __init__(self, tr_soup):
        torrent_seeders = tr_soup.find('td', {'class':'tlistsn'})  #gets seeders of torrent

        self.seeders = findSeeders(torrent_seeders)
        self.url = tr_soup.find('td', {'class':'tlistdownload'}).a['href']  #gets link to download torrent directly
        self.name = tr_soup.find('td', {'class':'tlistname'}).a.contents[0]  #gets name of torrent
        size_text = tr_soup.find('td', {'class':'tlistsize'}).contents[0]
        self.size = getTorrentSize(size_text)                                #computes the size of the torrent in kilobytes

        self.is_series = isTorrentSeries(self.name)
        if not self.is_series:                  #doesnt make sense to set episode number if it's a complete series.
            self.episode_number = findEpisodeNumber(self.name)

        self.is_aplus = findAPlus(tr_soup)


    #Get-methods, don't know if this is the standard in Python
    def getIsSeries(self):
        return self.is_series
    def getEpisode(self):
        return self.episode_number
    def getUrl(self):
        return self.url
    def getName(self):
        return self.name
    def getSize(self):
        return self.size
    def getSeeders(self):
        return self.seeders
    def getIsAplus(self):
        return self.is_aplus

####METHODS THAT ARE CALLED ON INIT OF TORRENT-OBJECT ######

#example: 258.3 MB, 13.7 GB, 200 KB
#returns size as float in KB size
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

def isTorrentSeries(torrent_name):
    series_regex = re.compile('((\d+)-(\d+))')    #a series torrent is usually specified by ep 1-400 for example
    if re.search(series_regex, torrent_name) is not None:
        return True
    else:
        return False

def findEpisodeNumber(torrent_name):
    try:
        array = re.split('(\d+)',torrent_name) #episode-number should i 95% of the cases be the first number after some text.
        return int(array[1])
    except:
        return 0

def findSeeders(torrent_seeders):
    try:
        seeders = torrent_seeders.contents[0]
        return int(seeders)
    except:
        return 0

def findAPlus(tr_soup):
    try:
        return tr_soup['class'][0] == 'aplus'   #checks for the aplus tlistrow class-tag on nyaa.se
    except:
        False

