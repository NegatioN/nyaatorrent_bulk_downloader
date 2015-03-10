from unittest import TestCase

__author__ = 'NegatioN'

import os
from nyaatorrent_downloader import config

class TestReadFromFile(TestCase):
    def setUp(self):
        if os.path.isfile("configs"):
            print("File exists")
        else:
            print("File does not exist")

        self.resolution = 720
        self.favorite = "Horriblesubs"
        self.threshold = 5
        self.prompt = False
        self.config = config.Configuration(self.resolution, self.favorite, self.threshold, self.prompt)

        self.config.save()
    def test_readFromFile(self):
        configs = config.readFromFile()
        print(configs.output())
        self.failUnless(self.resolution == configs.resolution)
        self.failUnless(self.favorite == configs.favorite_subber)
        self.failUnless(self.threshold == configs.fav_threshold)
        self.failUnless(self.prompt == configs.prompt)