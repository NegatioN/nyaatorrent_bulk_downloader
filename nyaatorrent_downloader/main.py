#!/usr/bin/env python

__author__ = 'NegatioN'

import os

from nyaatorrent_downloader import print_factory, parse_site, downloader, config, print_configs

global configs

## gets a settings-profile from .ini
def defineConfigs():
    global configs
    configs = config.readFromFile()
    if configs == None:
        configs = print_factory.createNewConfig()
    else:
        profile = print_factory.selectProfile(configs)
        configs.setProfile(profile)

#TODO create setting for searching non-english subbed anime

def run():
    global configs
    os.system("mode con: cols=135 lines=50") #forces console-size to be at least 135 columns.

    baseurl = "http://www.nyaa.se/?page=search&cats=1_37&filter=0&term="
    # if seeders are over a threshold.


    input = print_factory.start()

    #define resolution to avoid errors.
    resolution = 0

    #we have configs and want to load these.
    if configs != None:
        if configs.getPrompt() == False:  #user wants to use configs.
            resolution = configs.getResolution()
        else:                              #user wants to be prompted every time.
            resolution = print_factory.select_resolution()
    #we have no config-file and have to manually select options
    else:
        resolution = print_configs.select_resolution()
    print("searching...")



    sorted_series_list = parse_site.parse_query(baseurl, input, resolution, configs)

    print_factory.printSeries(sorted_series_list)

    selected_series = print_factory.chooseTorrent(sorted_series_list, configs)

    #if user didnt select back to menu
    if selected_series != None:
        downloader.download_series(sorted_series_list[selected_series])



    run() #loop untill escaped by user-input (input q in print-factory)

defineConfigs()

run()