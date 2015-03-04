# nyaatorrent_bulk_downloader
==================
A program to download entire series of torrents with one click from nyaa.se

Here are some examples of output:

![Example 1](https://raw.githubusercontent.com/NegatioN/nyaatorrent_bulk_downloader/master/screenshots/example1.PNG)
![Example 2](https://raw.githubusercontent.com/NegatioN/nyaatorrent_bulk_downloader/master/screenshots/example2.PNG)

## Download
Go to the ["Release tab"](https://github.com/NegatioN/nyaatorrent_bulk_downloader/releases ) for downloads


## Install
Use ```pip install``` to install the dependencies
pip install beautifulsoup4 requests colorama tabulate termcolor



## Objective
My objective with this program is to let the user be able to select from all series matching console-input and download all torrents for this given series.
Also the user should be able to select a resolution for the torrent to download.

My program "BulkTorrentDownloader" in theory already does these things, but through another site which requires a lot more HTTP GET-calls, and has a lot less versatility.
