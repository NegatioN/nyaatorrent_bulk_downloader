__author__ = 'NegatioN'

import os
import configparser

#the file takes care of saving a configuration-object to disk
#it also reads from the disk if the user wants to use config.
#TODO implement functionality in regex for favorite_subber. Add another color to that series in output.
#TODO implement several different users. in readFromFile only get current user's configs.

class Configuration:
    def __init__(self, config_dict):
        self.config_dict = config_dict

    #constructor from file
    @classmethod
    def fromfile(cls, config_list):
        resolution = int(config_list[0].strip())
        favorite_subber = config_list[1].strip()
        fav_threshold = int(config_list[2].strip())
        prompt = config_list[3].strip() == "True"       #if True, prompt True
        return cls(resolution, favorite_subber, fav_threshold, prompt)
    @classmethod
    def fromoptions(cls, resolution, favorite_subber, fav_threshold, prompt_for_config):
        dictionary = {}
        dictionary['DEFAULT'] = {'resolution' : 720, 'favorite_subber' : "[HorribleSubs]",
                                 'fav_threshold' : 10, 'prompt_on_query' : True}
        dictionary['USER'] = {'resolution' : resolution, 'favorite_subber' : favorite_subber,
                         'fav_threshold' : fav_threshold, 'prompt_on_query' : prompt_for_config}
        #resolution as int.
        #name of favorite subbers
        #threshold of seeders to let user select torrents from fav_subber
        #promt user for config every time program starts?
        return cls(dictionary)

    def getPrompt(self):
        return self.config_dict.getboolean('DEFAULT', 'prompt_on_query')
    def getResolution(self):
        return int(self.config_dict['DEFAULT']['resolution'])
    def getFavorite(self):
        return self.config_dict['DEFAULT']['favorite_subber']
    def getThreshold(self):
        return self.config_dict['DEFAULT']['fav_threshold']

    #outputs a list-item for each option with [name - value]
    def output(self):
        output = []
        tuples = self.getEditConfigs()
        for tuple in tuples:
            output.append(tuple[0] + " : " + str(tuple[1]))
        return output

    #returns tuples to be used to create a new configuration-object and save it
    def getEditConfigs(self):
        config_tuples = []
        for user in self.config_dict:       #gets each section in .ini
            for key in self.config_dict[user]:  #finds list of ini-keys
                config_tuple = key, self.config_dict[user][key]
                config_tuples.append(config_tuple)
            return config_tuples


    #writes the output of a config to a new file with the name configs.
    #saves configs in same folder as program.
    def save(self):
        config = configparser.ConfigParser()
        config.read_dict(self.config_dict)
        with open('configs.ini', 'w') as configfile:
            config.write(configfile)


#returns a configuration if it exists, otherwise returns None
def readFromFile():
    if os.path.isfile('configs.ini'):                   #only construct object if we have a config-file
        config = configparser.ConfigParser()
        config.read('configs.ini')
        return Configuration(config)
    else:
        print("returning None")
        return None



