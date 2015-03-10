__author__ = 'NegatioN'

import tabulate
import sys
from colorama import init
from termcolor import colored
from nyaatorrent_downloader import config

def start():
    helper()
    return input_query()

def helper():
    print("\nSearch torrents from Nyaa.se")

def input_query():
    query = input('>>')
    return query

def select_torrent(max_index):
    torrent = input('>> ')
    torrent = torrent.lower()   #simplify input-checks.
    try:
        index = int(torrent)
        if index > 0 and index < max_index+1:
            return index-1  #returns proper index in array compared to display
        else:
            print('The number you wrote is not present in the list...')
            select_torrent(max_index)
    except:
        if torrent == 'q':
            return torrent
        elif torrent == 'm':
            return torrent
        elif torrent == 'c':
            print("\n[ V ]iew settings, or [ C ]onfigure settings?")
            view_or_set = input()
            if view_or_set.lower() == 'v':
                viewConfigs()
                return
            else:
                setConfigs()
                return
        else:
            print('Please input a number...')
            select_torrent(max_index)


def select_resolution():
    arr = [480, 720, 1080]
    print("Write 1 for 480p, 2 for 720p or 3 for 1080p")
    userin = input("Please select resolution: \n>>")
    ##verify that input is integer
    try:
        index = int(userin)
        ##verify that input is in correct range
        if index < 4 and index > 0:
            return arr[index-1]
        else:
            print("Write a number from 1-3")
            select_resolution()
    except:
        print("Write a number from 1-3")
        select_resolution()


def printSeries(sorted_series):
    if sys.platform == 'win32':
        init()              #init colors for win32
    tabluate_list = []
    ##define headers of table
    number = "No."
    title = "Title"
    seeders = "Avg. Seeders"
    torrents = "Torrent-files"
    size = "Total Size"

    for index, series in enumerate(sorted_series):
        row = createSeriesRow(index,series)
        tabluate_list.append(row)
    output = tabulate.tabulate(tabluate_list, headers=[number,title, seeders, torrents, size])
    print(output)

def chooseTorrent(sorted_series):
    print('\nSelect series: [ 1 - ' + str(len(sorted_series)) + ' ] or [ S ] to search again, [ C ] to access configs or [ Q ] to quit')
    torrent = select_torrent(len(sorted_series))

    if torrent == 'q':
        sys.exit(0)
    elif torrent == 's':
        return
    elif torrent == 'c':
        return
    else:
        return torrent


def setConfigs():
    resolution = select_resolution()
    favorite = input("\nFavorite sub-group?")
    threshold = input("\nThreshold?")
    prompt = input("\nDo you want to be propmpted every time for settings?")
    configs = config.Configuration(resolution, favorite,threshold,prompt)

    configs.save()


def viewConfigs():
    configs = config.readFromFile()
    if configs != None:
        print("TEST")
        print(configs.output())



#outputs a color and size-formated text-tuple of a series-object
def createSeriesRow(index, series):
    attributes = [] #empty attributes if normal row
    if index % 2 == 1:
        attributes = ['bold']  #bold row attributes

    number = colored(str(index+1), attrs=attributes)

    name = colored(series.getName(), evaluateNameColor(series), attrs=attributes)
    seeders = colored(series.getAvgSeederString(), evaluateHealth(series), attrs=attributes)
    size = colored(series.getSizeString(),'white', attrs=attributes)
    torrents = colored(str(series.getNumberOfTorrents()),'white', attrs=attributes)

    row = (number ,name, seeders,torrents, size)
    return row

#evaluates the color output of average seeders
def evaluateHealth(series):
    number = series.getAverageSeeders()
    if number > 20:
        return 'green'
    elif number > 10:
        return 'yellow'
    else:
        return 'red'

#evaluates color of series-name. blue if aplus-content
def evaluateNameColor(series):
    if series.getIsAplus():
        return 'blue'
    else:
        return 'white'