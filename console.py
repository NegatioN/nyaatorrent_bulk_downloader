__author__ = 'NegatioN'

import print_factory
import parse_site

def run():
    baseurl = "http://www.nyaa.se/?page=search&cats=1_37&filter=0&term="

    input = print_factory.start()
    resolution = print_factory.select_resolution()
    print("searching...")



    sorted_series_list = parse_site.parse_query(baseurl, input, resolution)

    print_factory.printSeries(sorted_series_list)



    #run() #loop untill broken