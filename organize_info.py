__author__ = 'NegatioN'

import regex_treatment as rt
import torrent as tor
import re
#TODO remove duplicate episeodes.
#TODO let user choose resolution to download.
#TODO if series has a file with "All episodes", keep only this? or archive separately
#TODO implement console-input

#sorts all tuples into lists for their respective series, within a dictionary
#takes in a tuple with download_url, torrent_name, torrent_size
def organizeTorrentsToSeries(torrents):
    series_dictionary = {} #dict holding all series -> torrents within series

    for torrent in torrents:
        if torrent.getSeeders() > 0:                            #disregards the torrent if it has 0 seeders
            series_name = rt.findSeriesName(torrent.getName()) #get name of series from torrent_name
            print(series_name)
            if rt.isCorrectResolution(torrent.getName(), 720):  #only keep torrents containing the given resolution. 720p 360p etc.

                if series_name not in series_dictionary:
                    series_dictionary[series_name] = [] #create new list for given series in dictionary
                if not rt.episodeAlreadyAdded(series_dictionary[series_name], torrent.getEpisode()):
                    series_dictionary[series_name].append(torrent)  #add torrent-object to the dictionary list for it's series

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

