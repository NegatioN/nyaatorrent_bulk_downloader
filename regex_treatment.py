__author__ = 'NegatioN'

import re

#finds the name of a series based on the naming-convention [Subgroup] name - episode
def findSeriesName(torrent_name):
    string_array = re.split('(]|-)',torrent_name)
    if len(string_array) > 2:
        return string_array[2].strip().lower()  #for now index 2 should be the title. strip to remove trailing whitespace
    else:
        return torrent_name.lower()



#determines if the current torrent_name tested has the resolution we want
def isCorrectResolution(torrent_name, resolution):  #takes string, int
    resolution = str(resolution) + 'p'  #example 720 becomes 720p
    regex = re.compile(resolution)
    if regex.search(torrent_name) is not None:
        return True
    else:
        return False


#takes in a single series, and episode-number
#Checks if the episode has already been added to the series-list of torrents
def episodeAlreadyAdded(series, in_episode):
    for torrent in series:
        if in_episode == torrent.getEpisode():
            return True
    return False


#takes in string url, split its and returns the digit at the end.
def getPageNumber(anchor):
    array = re.split('(\d+)',anchor)

    return int(array[-2])    #leaves a trailing whitespace? so we go 2 indices back
#TODO create regex that checks if query actually exists in torrents series-name, not sub-group