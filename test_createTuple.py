from unittest import TestCase

__author__ = 'NegatioN'

import parse_site

#TODO find a good way to test this in a real environment.
#currently you just know from readouts that this matches what you want.
class TestCreateTuple(TestCase):
    def setUp(self):
        max = 5
        current = 0
        self.cases = []
        page_soup = parse_site.getAllSoup("http://www.nyaa.se/?page=search&term=", "sengoku").pop()
        table = page_soup.find_all("table", {'class': 'tlist'})
        #TODO get td class tlistname, tlistdownload, tlistsize, tlisticon -> a == http://www.nyaa.se/?cats=1_37  (english)
        #for td in page_soup.findAll('td'):
        for td in table:
            for tr in td.find_all("tr"): #each row
                for a in tr.find_all('a', {'href': 'http://www.nyaa.se/?cats=1_37'}): #for each tr in category "English subbed"
                    if current < max:
                        self.cases.append(tr)
                        current +=1
                    else:
                        break

        self.case1 = self.cases.pop()
        print(self.case1)
        self.case2 = self.cases.pop()
        print(self.case2)
        self.case3 = self.cases.pop()
        print(self.case3)
        self.case4 = self.cases.pop()
        print(self.case4)
        self.case5 = self.cases.pop()
        print(self.case5)

        return 0
    def test_createTuple(self):
        parse_site.createTuple(self.case1)
        parse_site.createTuple(self.case2)
        parse_site.createTuple(self.case3)
        parse_site.createTuple(self.case4)
        parse_site.createTuple(self.case5)

        self.fail()



