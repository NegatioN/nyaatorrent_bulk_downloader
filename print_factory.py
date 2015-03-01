__author__ = 'NegatioN'

import tabulate
import sys
import os
from colorama import init
from termcolor import colored, cprint

class TextFormat:
    BOLD = '\033[1m'
    NORMAL = '\033[0m'
    BOLD_GREEN = '\033[1m\033[32m'
    GREEN = '\033[0m\033[32m'
    RED = '\033[0m\033[31m'
    BOLD_RED = '\033[1m\033[31m'


def start():
    helper()
    return select_torrent()

def helper():
    print("\nSearch torrents from Nyaa.se")

def select_torrent():
    torrent = input('>> ')
    return torrent


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


#TODO apply colors and boldness in table
def printSeries(sorted_series):
    #init()              #init colors for win32
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


def finalize(titleSizeLink):
        # torrent selection
    print('\nSelect series: [ 1 - ' + str(len(titleSizeLink)) + ' ] or [ M ] to go back to main menu or [ Q ] to quit')
    torrent = select_torrent()
    if torrent == 'Q' or torrent == 'q':
        sys.exit(0)
    elif torrent == 'M' or torrent == 'm':
        return
    else:
        if int(torrent) <= 0 or int(torrent) > len(titleSizeLink):
            print('The number you wrote is not present in the list...')
        else:
            tri = titleSizeLink.__getitem__(int(torrent)-1)
            path = arrangeTorrents.createFolder(tri[0], "torrents")
            os.chdir(path)
            downloadTorrents.download_all_torrents(tri[1])
#finalize for titles input
#def finalize():

#outputs a color and size-formated text-tuple
def createSeriesRow(index, series):
    attributes = [] #empty attributes if normal row
    if index % 2 == 1:
        attributes = ['bold']  #bold row attributes

    number = colored(str(index+1), attrs=attributes)

    name = colored(series.getName(), evaluateNameColor(series), attrs=attributes)
    seeders_health = evaluateHealth(series.getAverageSeeders())
    seeders = colored(series.getAvgSeederString(), seeders_health, attrs=attributes)
    size = colored(series.getSizeString(), attrs=attributes)
    torrents = colored(str(series.getNumberOfTorrents()), attrs=attributes)

    row = (number ,name, seeders,torrents, size)
    return row

#evaluates the color output of average seeders
def evaluateHealth(number):
    if number > 20:
        return 'green'
    elif number > 10:
        return 'yellow'
    else:
        return 'red'

def evaluateNameColor(series):
    if series.getIsAplus():
        return 'blue'
    else:
        return 'grey'