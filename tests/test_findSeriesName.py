from unittest import TestCase

__author__ = 'NegatioN'

import regex_treatment as rt

class TestFindSeriesName(TestCase):
    def setUp(self):
        self.torrentName = "[FFF] Juuou Mujin no Fafnir - 07 [EFF619CA].mkv"
        self.clippedTorrentName = "Juuou Mujin no Fafnir"
        self.torrentName2 = "[Watashi]_Parasyte_-_the_maxim_-_04_[720p][A7E97910].mkv"
        self.clippedTorrentName2 = "Parasyte"

    def test_findSeriesName(self):
        value = rt.findSeriesName(self.torrentName)
        print(value)
        self.failUnless(self.clippedTorrentName == value)
        value = rt.findSeriesName(self.torrentName2)
        print(value)
        self.failUnless(self.clippedTorrentName2 == value)