__author__ = 'NegatioN'

class Series:

    def __init__(self, series_name ):
        self.name = series_name
        self.torrent_list = []

    #Adds a torrent to the torrent_list if it's missing
    def addTorrent(self, torrent):
        if not episodeAlreadyAdded(self.torrent_list, torrent.getEpisode()): #add episode only if it's missing.
            #print(self.name + " added: " + torrent.getName())
            self.torrent_list.append(torrent)

    ### GETTERS AND SETTERS ####
    def getName(self):
        return self.name
    def getTorrents(self):
        return self.torrent_list
    #outputs the size of a series in float, number of GB's
    def getSize(self):
        totalSize = 0
        for torrent in self.torrent_list:
            totalSize += torrent.getSize()
        return totalSize/1024/1024   #outbout gb

    #returns the average seeder number. Total_seeders/list.length
    def getAverageSeeders(self):
        total_seeders = 0
        for torrent in self.torrent_list:
            total_seeders += torrent.getSeeders()

        return (total_seeders/len(self.torrent_list))


#takes in a single series, and episode-number
#Checks if the episode has already been added to the series-list of torrents
def episodeAlreadyAdded(torrent_list, episode_number):
    for torrent in torrent_list:
        if episode_number == torrent.getEpisode():
            return True
    return False


#Test-method toString()
def printEpisodes(torrent_list):
    for torrent in torrent_list:
        print(torrent.getName())