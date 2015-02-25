# nyaatorrent_bulk_downloader
A program to download entire series of torrents with one click from nyaa.se

My objective with this program is to let the user be able to select from all series matching console-input and download all torrents(preferrably just one of each episode) for this given series.
Also the user should be able to select a resolution for the torrent to download.

My plan for doing this is currently relying in large part, on regex-checking names of torrents after getting the soup of all pages with relevant torrents.

My program "BulkTorrentDownloader" in theory already does these things, but through another site which requires a lot more HTTP GET-calls, and has a lot less versatility.
