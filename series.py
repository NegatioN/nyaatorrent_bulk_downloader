__author__ = 'NegatioN'

class Series:

    def __init__(self, series_name ):
        self.name = series_name
        self.torrent_list = []
        self.seeders = 0
        self.size = 0
        self.is_aplus = False

    #Adds a torrent to the torrent_list if it's missing
    def addTorrent(self, torrent):
        if not episodeAlreadyAdded(self.torrent_list, torrent.getEpisode()): #add episode only if it's missing.
            #print(self.name + " added: " + torrent.getName())
            self.torrent_list.append(torrent)
            self.size += torrent.getSize()
            self.seeders += torrent.getSeeders()


    ### GETTERS AND SETTERS ####
    def getName(self):
        return self.name
    def getIsAplus(self):
        return self.is_aplus
    def getTorrents(self):
        return self.torrent_list
    def getNumberOfTorrents(self):
        return len(self.torrent_list)
    #outputs the size of a series in float, number of GB's
    def getSize(self):
        return self.size/1024/1024   #outbout gb
    def setIsAplus(self):
        self.is_aplus = True

    #returns the average seeder number. Total_seeders/list.length
    def getAverageSeeders(self):
        return (self.seeders/len(self.torrent_list))
    def getSizeString(self):
        return u'{0:.2f}'.format(self.getSize())  + " GB"           #must output unicode-compatible strings for prettytable
    def getAvgSeederString(self):
        return u'{0:.2f}'.format(self.getAverageSeeders())  #must output 0 decimals for tabulate
    def toString(self):
        return self.name + " - " + str(len(self.torrent_list)) + " torrents - " + self.getAvgSeederString() + " average seeders - " + self.getSizeString() + " GiB"


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