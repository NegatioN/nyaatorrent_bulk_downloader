__author__ = 'NegatioN'

import requests
import os

def download_series(series):
    #TODO implement setting for where you wanna save torrents
    series_name = series.getName()
    path = createFolder(series_name, "torrents")
    oldPath = os.getcwd()       #used to get back to cwd
    os.chdir(path)      #changes current working directory to curDir/torrents/series-name
    for torrent in series.getTorrents():
        download_torrent(torrent.getName(), torrent.getUrl())

    #reset working directory to what we had before saving torrents
    os.chdir(oldPath)


#Downloads a single torrent file.
def download_torrent(title, url):
    print('Downloading >> ' + title)
    fname = os.getcwd() + os.sep + title + '.torrent'
    # http://stackoverflow.com/a/14114741/1302018
    try:
        r = requests.get(url, stream=True)
        with open(fname, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
    except requests.exceptions.RequestException as e:
        print('\n' + str(e) + '\nSomething went wrong with file: ' + title)
        print("Failed. Trying next torrent.")

    return fname



#get contents of an url
def getContents(url):
    try:
        cont = requests.get(url)
    except requests.exceptions.RequestException as e:
        raise SystemExit('\n' + str(e))
    return cont

#creates a folder within current working dir
#returns path of dir
def createFolder(name, path): #name of folder, and a default sub-folder you want to add
    path=os.getcwd() + os.sep + path + os.sep + name
    if not os.path.isdir(path):
        os.makedirs(path)
    return path
