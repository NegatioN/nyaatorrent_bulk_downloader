from unittest import TestCase

__author__ = 'NegatioN'

import parse_site

class TestOrganizeTorrentsToSeries(TestCase):

    def setUp(self):
        self.torrentName = "[FFF] Juuou Mujin no Fafnir - 07 720p [EFF619CA].mkv"
        self.clippedTorrentName = "Juuou Mujin no Fafnir"
        self.series = []
        self.series.append(self.torrentName)

    def test_organizeTorrentsToSeries(self):
        series = parse_site.organizeTorrentsToSeries(self.series)
        print(series)
        self.failUnless(series[self.clippedTorrentName].pop() == self.torrentName)