__author__ = 'NegatioN'

import regex_treatment as rt
import torrent as tor
import re
import series as ser
#TODO remove duplicate episeodes.
#TODO let user choose resolution to download.
#TODO if series has a file with "All episodes", keep only this? or archive separately
#TODO implement console-input
#TODO implement stop parsing when we find a torrent with 0 seeders. we're searching through list sorted by seeders
#TODO append OVA's somewhere? to the series?


#sorts all tuples into lists for their respective series, within a dictionary
#takes in a tuple with download_url, torrent_name, torrent_size
def organizeTorrentsToSeries(torrents):
    series_dictionary = {} #dict holding all series -> torrents within series

    for torrent in torrents:
        if torrent.getSeeders() > 0:                            #disregards the torrent if it has 0 seeders
            series_name = rt.findSeriesName(torrent) #get name of series from torrent
            if rt.isCorrectResolution(torrent.getName(), 720):  #only keep torrents containing the given resolution. 720p 360p etc.
                if torrent.getIsSeries():
                    series_name = torrent.getName()
                if torrent.getIsAplus():
                    series_name = series_name + " A+ content"
                if series_name not in series_dictionary:
                    series_dictionary[series_name] = ser.Series(series_name) #create a new series-object
                series_dictionary[series_name].addTorrent(torrent)

    return series_dictionary
        #Standard naming convention seems to be [subgroup] seriesname     episode etc



#takes in the soup of a single page, a list to append tuples to
#returns a list of all torrents that match search with url, name, size(in kb), seeders
def createTorrentList(page_soup, torrents):
    #STRUCTURE = Tbody -> tr class tlistrow -> tds
    table = page_soup.find_all("table", {'class': 'tlist'})

    for list in table:
        for tr in list.find_all("tr", {'class':re.compile('.*(tlistrow).*')}): #each row that contains a torrent
            torrents.append(tor.Torrent(tr)) #creates a new torrent-object of the tr_soup

    return torrents

