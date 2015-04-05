from unittest import TestCase

__author__ = 'NegatioN'

from nyaatorrent_downloader import torrent as tor

class TestFindGroupName(TestCase):
    def setUp(self):
        self.torrentName = "[Taka]_Naruto_Shippuuden_177_[720p][6EC1F800].mp4"
        self.torrentSubber = "taka"
    def test_findGroupName(self):
        self.failUnless(tor.findGroupName(self.torrentName) == self.torrentSubber)