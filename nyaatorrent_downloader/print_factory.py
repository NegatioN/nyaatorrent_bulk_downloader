__author__ = 'NegatioN'

import tabulate
import sys
from colorama import init
from termcolor import colored
from nyaatorrent_downloader import print_configs

def start():
    helper()
    return input_query()

def helper():
    print("\nSearch torrents from Nyaa.se")

def input_query():
    query = input('>>')
    return query

def select_torrent(max_index, configs):
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
            print("\n[ V ] to view settings, [ M ] to make a new profile, or [ C ] to configure settings\n>>")
            view_or_set = input()
            if view_or_set.lower() == 'v':
                viewConfigs(configs)
                return
            elif view_or_set.lower() == 'm':
                createNewConfig()
                return
            else:
                setConfigs(configs)
                return
        else:
            print('Please input a number...')
            select_torrent(max_index)



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

def chooseTorrent(sorted_series, configs):
    print('\nSelect series: [ 1 - ' + str(len(sorted_series)) + ' ] or [ S ] to search again, [ C ] to access configs or [ Q ] to quit')
    torrent = select_torrent(len(sorted_series), configs)

    if torrent == 'q':
        sys.exit(0)
    elif torrent == 's':
        return
    elif torrent == 'c':
        return
    else:
        return torrent




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

def viewConfigs(configs):
    print_configs.viewConfigs(configs)
def setConfigs(configs):
    print_configs.setConfigs(configs)
def createNewConfig():
    return print_configs.createNewConfig()
def selectProfile(configs):
    return print_configs.selectProfile(configs)
