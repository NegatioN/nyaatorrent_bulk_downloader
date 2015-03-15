__author__ = 'NegatioN'

from nyaatorrent_downloader import config

#Edit settings of the selected profile.
def setConfigs(configs):
    configuration = config.readFromFile()

    if configuration == None:
        print("There doesn't seem to be any configs yet.\n")
        return
    profileName = configs.getCurrentProfile()
    profile_dict = createConfigDict()
    configs.insertProfile(profile_dict, profileName)
    viewConfigs(configs)

def createNewConfig():
    wantToCreate = input("Do you want to create new configs?\n>>").lower()
    if wantToCreate == 'yes' or wantToCreate == 'y':
        configs = makeConfig()
        viewConfigs(configs)
        return configs
    return None

#makes a new config-profile.
def makeConfig():
    configuration = config.readFromFile()

    profileName = input("Write a profile-name\n>>")
    profile_dict = createConfigDict()

    #Does a set of configuration exist from before?
    if configuration == None:
        configs = config.Configuration.fromoptions(profileName,profile_dict)
        configs.setProfile(profileName)
        configs.save()
        return configs
    else:
        configuration.insertProfile(profile_dict, profileName)
        return configuration

#Output configs of current user to console
def viewConfigs(settings):
    configs = config.readFromFile()
    if configs != None:
        profileName = settings.getCurrentProfile()
        print("Settings for: " + profileName)
        output = configs.output(profileName)
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

#selects a profile for use throughout the program-cycle
def selectProfile(configs):
    profiles = configs.getProfiles()
    num = 1
    for profile in profiles:
        print(str(num) + " - " + profile)
        num += 1
    userin = input("Select one of the profiles from 1 - " + str(num-1) + "\n>>")
    try:
        index = int(userin)-1
        if index < num-1 and index > 0:
            selected_profile = profiles[index]
            return selected_profile
        else:
            print("Write a number from 1-" + str(len(profile)))
            selectProfile(configs)
    except:
        print("Write a number from 1-" + str(len(profile)))
        selectProfile(configs)

def createConfigDict():
    resolution = select_resolution()
    favorite_subber = input("What's your favorite sub-group?\n>>")
    try:
        threshold = int(input("How many seeders should the group have for it to appear?\n>>"))
    except:
        threshold = int(input("How many seeders should the group have for it to appear?\n>>"))
    prompt = input("Do you want to be prompted for resolution before each search? yes/no\n>>")

    profileDict = {'resolution' : resolution, 'favorite_subber' : favorite_subber,
               'fav_threshold' : threshold, 'prompt_on_query' : prompt}

    return profileDict
