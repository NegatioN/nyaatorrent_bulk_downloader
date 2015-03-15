__author__ = 'NegatioN'

from nyaatorrent_downloader import config

def setConfigs():
    configuration = config.readFromFile()

    if configuration == None:
        print("There doesn't seem to be any configs yet.\n")
        return
    config_tuples = configuration.getEditConfigs()

    newSettings = {}
    newSettings['DEFAULT'] = {}
    for configs in config_tuples:
        currentSetting = configs[0]
        if currentSetting == 'resolution':
            newInput = select_resolution()
        else:
            newInput = input(currentSetting + "\n>>")

        newSettings['DEFAULT'][currentSetting] = newInput

    configs = config.Configuration(newSettings)
    configs.save()
    viewConfigs()

def createNewConfig():
    wantToCreate = input("Do you want to create new configs?\n>>").lower()
    if wantToCreate == 'yes' or wantToCreate == 'y':
        makeConfig()
        viewConfigs()

def makeConfig():
    profileName = input("Write a profile-name\n>>")
    config_dict = {}
    config_dict[profileName] = {}
    resolution = select_resolution()
    favorite_subber = input("What's your favorite sub-group?\n>>")
    try:
        threshold = int(input("How many seeders should the group have for it to appear?\n>>"))
    except:
        threshold = int(input("How many seeders should the group have for it to appear?\n>>"))
    prompt = input("Do you want to be prompted for resolution before each search?\n>>")

    configs = config.Configuration.fromoptions(profileName,resolution,favorite_subber,threshold, prompt)
    configs.setProfile(profileName)
    configs.save()

def viewConfigs():
    configs = config.readFromFile()
    if configs != None:
        output = configs.output()
        for setting in output:
            print(setting)
    else:
        print("No settings are currently saved.")

def select_resolution():
    arr = [480, 720, 1080]
    print("Write 1 for 480p, 2 for 720p or 3 for 1080p")
    userin = input("Please select resolution: \n>>")
    ##verify that input is integer
    try:
        index = int(userin)
        ##verify that input is in correct range
        if index < 4 and index > 0:
            return arr[index-1]
        else:
            print("Write a number from 1-3")
            select_resolution()
    except:
        print("Write a number from 1-3")
        select_resolution()

def selectProfile(configs):
    profiles = configs.getProfiles()
    num = 1
    for profile in profiles:
        print(str(num) + " - " + profile)
        num += 1
    try:
        selected_input = input("Select one of the profiles from 1 - " + str(num-1) + "\n>>")
        selected_profile = int(selected_input) - 1

    except:
        selected_input = input("Select one of the profiles from 1 - " + str(num-1) + "\n>>")
        selected_profile = int(selected_input) - 1
    return selected_profile
