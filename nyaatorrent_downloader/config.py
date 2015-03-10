__author__ = 'NegatioN'

import os
#the file takes care of saving a configuration-object to disk
#it also reads from the disk if the user wants to use config.
#TODO implement functionality in regex for favorite_subber. Add another color to that series in output.

class Configuration:
    def __init__(self, resolution, favorite_subber, fav_threshold, prompt_for_config):
        self.resolution = resolution            #resolution as int.
        self.favorite_subber = favorite_subber  #name of favorite subbers
        self.fav_threshold = fav_threshold      #threshold of seeders to let user select torrents from fav_subber
        self.prompt = prompt_for_config         #promt user for config every time program starts?

    #constructor from file
    @classmethod
    def fromfile(cls, config_list):
        resolution = int(config_list[0].strip())
        favorite_subber = config_list[1].strip()
        fav_threshold = int(config_list[2].strip())
        prompt = config_list[3].strip() == "True"       #if True, prompt True
        return cls(resolution, favorite_subber, fav_threshold, prompt)

    #outputs a string of configs
    def output(self):
        return str(self.resolution) + "\n" + self.favorite_subber + "\n" + str(self.fav_threshold) + "\n" + str(self.prompt)

    #writes the output of a config to a new file with the name configs.
    #saves configs in same folder as program.
    def save(self):
        config_file = open("configs", "w")
        config_file.write(self.output())
        config_file.close()

#returns a configuration if it exists, otherwise returns None
def readFromFile():
    if os.path.isfile("configs"):                   #only construct object if we have a config-file
        config_file = open("configs", "r")
        config_list = []
        for line in config_file:                    #gets all lines of options from config
            config_list.append(line)
        config_file.close()

        return Configuration.fromfile(config_list)  #creates a config from file
    else:
        print("returning None")
        return None



