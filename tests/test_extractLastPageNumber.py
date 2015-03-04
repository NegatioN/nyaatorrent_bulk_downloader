from unittest import TestCase

__author__ = 'NegatioN'

from nyaatorrent_downloader import parse_site


class TestGetPageNumber(TestCase):
    def setUp(self):
        self.case1 = "http://www.nyaa.se/?cats=1_38&offset=100"
        self.case2 = "http://www.nyaa.se/?page=search&cats=1_37&term=kill+la&offset=3"
    def test_getPageNumber(self):
        pagenum1 = parse_site.getPageNumber(self.case1)
        pagenum2 = parse_site.getPageNumber(self.case2)
        self.failUnless(pagenum1 == 100)
        self.failUnless(pagenum2 == 3)
        #self.fail()