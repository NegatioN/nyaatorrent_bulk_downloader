__author__ = 'NegatioN'

import tabulate
import sys
import os

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

#outputs the dictionary of series to a string with info about each series
def printSeriesList(sorted_series):
    i = 0
    for series in sorted_series:
        i += 1
        print("No. " + str(i) + " - " + series.toString())

def select_resolution():
    arr = [480, 720, 1080]
    print("Press 1 for 480p, 2 for 720p or 3 for 1080p")
    userin = input("select resolution >>")

    if int(userin) < 4 and int(userin) > 0:
        return userin
    else:
        print("Write a number 1-3")
        select_resolution()


def printTitle(titles):
    table = []
    for index, value in enumerate(titles):
        title, link = value
        if index % 2 == 0:
            row = OutColors.BW + str(index+1), OutColors.BW + title
        else:
            row = OutColors.DEFAULT + str(index+1), OutColors.DEFAULT + title
        table.append(row)
    print()
    print(tabulate.tabulate(table, headers=['No.', 'Title']))


def printTitleSize(titleSizeLink):
    print("YES")
    table = []
    #print table
    for index, value in enumerate(titleSizeLink):
        title, link, size = value
        #table format: index, title, size
        if index % 2 == 0:
            row = OutColors.BW + str(index+1) + OutColors.DEFAULT, OutColors.BW + title + OutColors.DEFAULT, OutColors.BW + size + OutColors.DEFAULT
        else:
            row = str(index+1), title, size
        table.append(row)
    print()
    print(tabulate.tabulate(table, headers=['No.', 'Title', 'Episodes']))


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

def select_resolution():
    arr = [480, 720, 1080]
    print("Press 1 for 480p, 2 for 720p or 3 for 1080p")
    userin = input("select resolution >>")

    if int(userin) < 4 and int(userin) > 0:
        return userin
    else:
        print("Write a number 1-3")
        select_resolution()

#defines if the user wants to include episode-counts
def select_check_epcount():
    userin = input("Do you want to check episode-count? y/n  >>")
    if userin == 'y' or userin == 'Y':
        return True
    else:
        return False