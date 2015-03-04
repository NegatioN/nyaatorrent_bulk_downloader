from unittest import TestCase

__author__ = 'NegatioN'

from nyaatorrent_downloader import regex_treatment as rt
import nyaatorrent_downloader.torrent as tor

class TestFindSeriesName(TestCase):
    def setUp(self):
        self.torrent = tor.Torrent()
        self.torrent.name = "[FFF] Juuou Mujin no Fafnir - 07 [EFF619CA].mkv"
        self.torrent.episode_number = 7
        self.clippedTorrentName = "Juuou Mujin no Fafnir"
        self.torrent2 = tor.Torrent()
        self.torrent2.name = "[Watashi]_Parasyte_-_the_maxim_-_04_[720p][A7E97910].mkv"
        self.torrent2.episode_number = 4
        self.clippedTorrentName2 = "Parasyte"
        self.torrent3 = tor.Torrent()
        self.torrent3.name = "[Taka]_Naruto_Shippuuden_177_[720p][6EC1F800].mp4"
        self.torrent3.episode_number = 177
        self.clippedTorrentName3 = "Naruto Shippuuden"

    def test_findSeriesName(self):
        value = rt.findSeriesName(self.torrent)
        print(value)
        self.failUnless(self.clippedTorrentName == value)
        value = rt.findSeriesName(self.torrent2)
        print(value)
        self.failUnless(self.clippedTorrentName2 == value)
        value = rt.findSeriesName(self.torrent3)
        print(value)
        self.failUnlesss(self.clippedTorrentName3 == value)