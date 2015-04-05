__author__ = 'NegatioN'

import re

from nyaatorrent_downloader import regex_treatment as rt
from nyaatorrent_downloader import torrent as tor
from nyaatorrent_downloader import series as ser

#TODO implement stop parsing when we find a torrent with 0 seeders. we're searching through list sorted by seeders
#TODO append OVA's somewhere? to the series?
#TODO implement A+ torrents can be in both favorite-subber and highest seeded content


#sorts all tuples into lists for their respective series, within a dictionary
#takes in a tuple with download_url, torrent_name, torrent_size
def organizeTorrentsToSeries(torrents, resolution, configs):
    series_dictionary = {} #dict holding all series -> torrents within series
    if configs != None:
        favorite_subber = configs.getFavorite()     #get favorite_subber from configs
    else:
        favorite_subber = None

    count = 0
    for torrent in torrents:
        if torrent.getSeeders() > 0:                                    #disregards the torrent if it has 0 seeders
            if rt.isCorrectResolution(torrent.getName(), resolution) or torrent.getIsAplus():  #only keep torrents containing the given resolution. 720p 360p etc.
                putTorrentInDict(torrent, series_dictionary, favorite_subber)
        #break if seeders are 0. this means all torrents after this should be 0, if we sort by seeders.
        else:
            return series_dictionary

    return series_dictionary



#takes in the soup of a single page, a list to append tuples to
#returns a list of all torrents that match search with url, name, size(in kb), seeders
def createTorrentList(page_soup, torrents):
    #STRUCTURE = Tbody -> tr class tlistrow -> tds
    table = page_soup.find_all("table", {'class': 'tlist'})

    for list in table:
        for tr in list.find_all("tr", {'class':re.compile('.*(tlistrow).*')}): #each row that contains a torrent
            torrents.append(tor.Torrent.fromsoup(tr)) #creates a new torrent-object of the tr_soup

    return torrents

#removes
def outputSeries(series_dictionary):
    sorted_series = []
    for key, series in series_dictionary.items():
        series_torrents = series.getTorrents()

        #only output series with more than 5 torrents, or complete series_torrents, or A plus
        if len(series_torrents) > 5 or series_torrents[0].getIsSeries() or series_torrents[0].getIsAplus():
            sorted_series.append(series)


    sorted_series.sort(key=lambda x: x.getAverageSeeders(), reverse=True) #sort list in place by seeders

    return sorted_series

#Defines the name of a series-listing in output based on configs and torrent.
def putTorrentInDict(torrent, series_dictionary, favorite_subber):
    series_name = rt.findSeriesName(torrent) #get name of series from torrent
    aplus = False       #if series is aplus content
    favorite = False    #is torrent from favorite subber?

    if torrent.getIsSeries():
        series_name = torrent.getName()
    if torrent.getIsAplus():
        series_name = series_name + " A+ content"
        aplus = True
    elif torrent.getSubGroup() == favorite_subber and favorite_subber != None:
        series_name = series_name + " [" + torrent.getSubGroup() + "]"
        favorite = True
    #is the series not represented in dict? then create new entry.
    if series_name not in series_dictionary:
        series_dictionary[series_name] = ser.Series(series_name) #create a new series-object
        if aplus:
            series_dictionary[series_name].setIsAplus()
        elif favorite:
            series_dictionary[series_name].setIsFavorite()

    series_dictionary[series_name].addTorrent(torrent)


