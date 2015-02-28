__author__ = 'NegatioN'

import print_factory as pf
import parse_site

def run():
    baseurl = "http://www.nyaa.se/?page=search&cats=1_37&filter=0&term="

    input = pf.start()
    print("searching...")

    sorted_series_list = parse_site.parse_query(baseurl, input, 720)

    pf.printSeriesList(sorted_series_list)



    #run() #loop untill broken