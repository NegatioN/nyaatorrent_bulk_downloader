__author__ = 'NegatioN'

import re

#TODO implement is_movie field, regex torrent for movie etc.
#TODO let be is_series if "Season x" regex match?

#this class represents a torrent, and contains all the information we want to track about it.
#constructor currently takes in a tr_soup from beautifulsoup4
class Torrent:

    #default-constructor
    def __init__(self, url, name, seeders, size, is_aplus):
        self.url = url
        self.name = name
        self.seeders = seeders
        self.size = size
        self.is_series = isTorrentSeries(name)
        self.sub_group = findGroupName(name)
        self.is_aplus = is_aplus


        if not self.is_series:                  #doesnt make sense to set episode number if it's a complete series.
            self.episode_number = findEpisodeNumber(self.name)
        else:
            self.episode_number = 0

    #dummy constructor to do tests of various methods.
    @classmethod
    def dummy(cls, torrent_name, episode):
        return cls(None, torrent_name, None, None, None)

    #creates a torrent-object from a BS4 TR-soup element. assumes nyaa.se syntax
    @classmethod
    def fromsoup(cls, tr_soup):

        torrent_seeders = tr_soup.find('td', {'class':'tlistsn'})  #gets seeders of torrent

        seeders = findSeeders(torrent_seeders)
        url = tr_soup.find('td', {'class':'tlistdownload'}).a['href']  #gets link to download torrent directly
        name = tr_soup.find('td', {'class':'tlistname'}).a.contents[0]  #gets name of torrent
        size_text = tr_soup.find('td', {'class':'tlistsize'}).contents[0]
        size = getTorrentSize(size_text)                                #computes the size of the torrent in kilobytes

        is_aplus = findAPlus(tr_soup)
        return cls(url, name, seeders, size, is_aplus)


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
    def getSubGroup(self):
        return self.sub_group

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
    complete_regex = re.compile(r'(complete)|(season)')
    if re.search(series_regex, torrent_name) is not None or re.search(complete_regex, torrent_name.lower()):
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
        return False

def findGroupName(torrent_name):
    string_array = re.split(r"\[(.*?)\]", torrent_name, re.IGNORECASE)   #ignore start of torrent (sub-group)
    try:
        return string_array[1].lower()
    except:
        return None

