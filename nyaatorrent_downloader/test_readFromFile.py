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
        self.favorite = "[HorribleSubs]"
        self.threshold = 10
        self.prompt = True

        dictionary = {}
        dictionary['DEFAULT'] = {'resolution' : self.resolution, 'favorite_subber' : self.favorite,
                                 'fav_threshold' : self.threshold, 'prompt_on_query' : self.prompt}
        self.config = config.Configuration(dictionary)
        self.config.save()

        self.config.save()
    def test_readFromFile(self):
        configs = config.readFromFile()

        output = configs.output()
        configs = configs.config_dict
        for line in output:
            print(line)
        self.failUnless(self.resolution == int(configs['DEFAULT']['resolution']))
        self.failUnless(self.favorite == configs['DEFAULT']['favorite_subber'])
        self.failUnless(self.threshold == int(configs['DEFAULT']['fav_threshold']))
        self.failUnless(self.prompt == configs.getboolean('DEFAULT', 'prompt_on_query'))