__author__ = 'NegatioN'

import regex_treatment as rt

#sorts all tuples into lists for their respective series, within a dictionary
#takes in a tuple with download_url, torrent_name, torrent_size
def organizeTorrentsToSeries(torrent_tuples):
    series_dictionary = {} #dict holding all series -> torrents within series


    for torrent_url,torrent_name,torrent_size, torrent_seeders in torrent_tuples:
        if torrent_seeders > 0:
            series_name = rt.findSeriesName(torrent_name)                  #get name of series from torrent_name
            if rt.isCorrectResolution(torrent_name,720):    #only keep torrents containing the given resolution. 720p 360p etc.

                if series_name not in series_dictionary:
                    #create new list for given series in dictionary
                    series_dictionary[series_name] = []
                tuple = torrent_url, torrent_name, torrent_size
                series_dictionary[series_name].append(tuple)     #add url to the dictionary list for it's series

    return series_dictionary
    #Should sort all tuples into lists for their respective series.
    #Should throw away torrents with 0 seeders
    #Must have a method for defining what series it belongs to based on name of torrent.
        #Standard naming convention seems to be [subgroup] seriesname     episode etc



#takes in the soup of a single page, a list to append tuples to
#returns a list of all torrents that match search with url, name, size(in kb), seeders
def createTorrentTuples(page_soup, tuples):
    #STRUCTURE = Tbody -> tr class tlistrow -> tds
    table = page_soup.find_all("table", {'class': 'tlist'})

    for td in table:
        for tr in td.find_all("tr"): #each row
            #for a in tr.find_all('a', {'href': 'http://www.nyaa.se/?cats=1_37'}): #for each tr in category "English subbed"
            tuples.append(createTuple(tr))

    return tuples

#returns a tuple with download_url, torrent_name, torrent_size, torrent_seeders
#takes in a soup-object's TR-row.
def createTuple(tr_soup):
    torrent_seeders = tr_soup.find('td', {'class':'tlistsn'})  #gets seeders of torrent
    if torrent_seeders is not None:
        torrent_seeders = int(torrent_seeders.contents[0])
    else:                               #if the site has failed to find number of seeders we disregard the torrent
        torrent_seeders = 0
    if torrent_seeders > 0:             #disregards parsing all other fields if there are 0 seeders
        download_url = tr_soup.find('td', {'class':'tlistdownload'}).a['href']  #gets link to download torrent directly
        torrent_name = tr_soup.find('td', {'class':'tlistname'}).a.contents[0]  #gets name of torrent
        size_text = tr_soup.find('td', {'class':'tlistsize'}).contents[0]
        torrent_size = rt.getTorrentSize(size_text)                                #computes the size of the torrent in kilobytes
    else:
        download_url = ""
        torrent_name = ""
        torrent_size = 0

    torrent_tuple = (download_url, torrent_name, torrent_size, torrent_seeders)                #compounds all fields into tuple

    return torrent_tuple

