#!/usr/bin/env python

__author__ = 'NegatioN'

import os

from nyaatorrent_downloader import print_factory, parse_site, downloader


def run():
    os.system("mode con: cols=135 lines=50") #forces console-size to be at least 135 columns.

    baseurl = "http://www.nyaa.se/?page=search&cats=1_37&filter=0&term="

    input = print_factory.start()
    resolution = print_factory.select_resolution()
    print("searching...")



    sorted_series_list = parse_site.parse_query(baseurl, input, resolution)

    print_factory.printSeries(sorted_series_list)

    selected_series = print_factory.chooseTorrent(sorted_series_list)

    #if user didnt select back to menu
    if selected_series != None:
        downloader.download_series(sorted_series_list[selected_series])



    run() #loop untill escaped by user-input

run()