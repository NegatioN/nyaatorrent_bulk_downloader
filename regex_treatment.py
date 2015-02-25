__author__ = 'NegatioN'

import re

#finds the name of a series based on the naming-convention [Subgroup] name - episode
def findSeriesName(url):
    string_array = re.split('(]|-)',url)
    if len(string_array) > 2:
        return string_array[2].strip().lower()  #for now index 2 should be the title. strip to remove trailing whitespace
    else:
        return url.lower()


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

#TODO create regex that checks if query actually exists in torrents series-name, not sub-group