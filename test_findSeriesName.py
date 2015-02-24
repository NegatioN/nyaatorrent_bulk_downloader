from unittest import TestCase

__author__ = 'NegatioN'

import parse_site

class TestFindSeriesName(TestCase):
    def setUp(self):
        self.torrentName = "[FFF] Juuou Mujin no Fafnir - 07 [EFF619CA].mkv"
        self.clippedTorrentName = "Juuou Mujin no Fafnir"

    def test_findSeriesName(self):
        value = parse_site.findSeriesName(self.torrentName)
        self.failUnless(self.clippedTorrentName == value)