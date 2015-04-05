from unittest import TestCase

__author__ = 'NegatioN'

from nyaatorrent_downloader import regex_treatment as rt
import nyaatorrent_downloader.torrent as tor

class TestFindSeriesName(TestCase):
    def setUp(self):
        self.torrent = tor.Torrent.dummy("[FFF] Juuou Mujin no Fafnir - 07 [EFF619CA].mkv", 7)
        self.clippedTorrentName = "Juuou Mujin no Fafnir".lower()
        self.torrent2 = tor.Torrent.dummy("[Watashi]_Parasyte_-_the_maxim_-_04_[720p][A7E97910].mkv", 4)
        self.clippedTorrentName2 = "Parasyte".lower()
        self.torrent3 = tor.Torrent.dummy("[Taka]_Naruto_Shippuuden_177_[720p][6EC1F800].mp4", 177)
        self.clippedTorrentName3 = "Naruto Shippuuden".lower()
        self.torrent4 = tor.Torrent.dummy("[BakedFish] Ansatsu Kyoushitsu (2015) - 06 [720p][AAC].mp4", 6)
        self.clippedTorrentName4 = "Ansatsu Kyoushitsu (2015)".lower()

    def test_findSeriesName(self):
        value = rt.findSeriesName(self.torrent)
        print(value)
        self.failUnless(self.clippedTorrentName == value)
        value = rt.findSeriesName(self.torrent2)
        print(value)
        self.failUnless(self.clippedTorrentName2 == value)
        value = rt.findSeriesName(self.torrent3)
        print(value)
        self.failUnless(self.clippedTorrentName3 == value)
        value = rt.findSeriesName(self.torrent4)
        print(value)
        self.failUnless(self.clippedTorrentName4 == value)

