from unittest import TestCase

__author__ = 'NegatioN'

import parse_site

class TestOrganizeTorrentsToSeries(TestCase):

    def setUp(self):
        self.torrentName = "[FFF] Juuou Mujin no Fafnir - 07 [EFF619CA].mkv"
        self.clippedTorrentName = "Juuou Mujin no Fafnir"
        self.urls = []
        self.urls.append(self.torrentName)

    def test_organizeTorrentsToSeries(self):
        series = parse_site.organizeTorrentsToSeries(self.urls)
        print(series[self.clippedTorrentName])
        self.failUnless(series[self.clippedTorrentName] == self.torrentName)