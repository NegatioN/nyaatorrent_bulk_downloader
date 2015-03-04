from unittest import TestCase

__author__ = 'NegatioN'

from nyaatorrent_downloader import torrent as tor, parse_site
import re

#TODO find a good way to test this in a real environment.
#currently you just know from readouts that this matches what you want.
class TestCreateTuple(TestCase):
    def setUp(self):
        max = 10
        current = 0
        self.cases = []
        page_soup = parse_site.getAllSoup("http://www.nyaa.se/?page=search&cats=1_37&filter=0&term=", "sengoku").pop()
        table = page_soup.find_all("table", {'class': 'tlist'})

        #for td in page_soup.findAll('td'):
        for list in table:
            for tr in list.find_all("tr", {'class':re.compile('.*(tlistrow).*')}): #each row

                    if current < max:
                        self.cases.append(tr)
                        current +=1
                    else:
                        break



        return 0
    def test_createTuple(self):
        for case in self.cases:
            torrent = tor.Torrent(case)
            print("url:" + torrent.getUrl() + " name: " + torrent.getName() + " size: " + str(torrent.getSize()))






