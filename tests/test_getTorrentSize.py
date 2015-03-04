from unittest import TestCase

__author__ = 'NegatioN'
from nyaatorrent_downloader import parse_site


class TestGetTorrentSize(TestCase):
    def setUp(self):
        self.case1 = "258.3 MiB"
        self.case2 = "13.7 GiB"
        self.case3 = "23 MiB"
        self.case4 = "255 KiB"
        self.case5 = "85"
        self.case6 = ""
    def test_getTorrentSize(self):
        self.failUnless(parse_site.getTorrentSize(self.case1) == (258.3*1024))
        self.failUnless(parse_site.getTorrentSize(self.case2) == (13.7*1024*1024))
        self.failUnless(parse_site.getTorrentSize(self.case3) == (23*1024))
        self.failUnless(parse_site.getTorrentSize(self.case4) == 255)
        self.failUnless(parse_site.getTorrentSize(self.case5) == 1)
        self.failUnless(parse_site.getTorrentSize(self.case6) == 0)