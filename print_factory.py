__author__ = 'NegatioN'

import tabulate
import sys
import os
from prettytable import PrettyTable

class OutColors:
    DEFAULT = '\033[0m'
    BW = '\033[1m'
    LG = '\033[0m\033[32m'
    LR = '\033[0m\033[31m'

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
    print(userin)
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

#TODO apply colors in table
def printSeries(sorted_series):
    ##define headers of table
    number = "No."
    title = "Title"
    seeders = "Avg. Seeders"
    size = "Total Size"
    #define prettyTable
    pretty_table = PrettyTable([number, title, seeders, size])
    pretty_table.padding_width = 1
    #left-align content
    pretty_table.align[title] = "l"
    pretty_table.align[seeders] = "l"
    pretty_table.align[size] = "l"

    #input content to table
    for index, series in enumerate(sorted_series):
        row = str(index+1), series.getName(), series.getAvgSeederString(), series.getSizeString()
        pretty_table.add_row(row)
    print(pretty_table)


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
