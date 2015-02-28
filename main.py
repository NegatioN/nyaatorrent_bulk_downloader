#!/usr/bin/env python

__author__ = 'NegatioN'


import parse_site
#TODO implement user choose resolution

baseurl = "http://www.nyaa.se/?page=search&cats=1_37&filter=0&term="


input = "naruto"
parse_site.test(baseurl, input)

url = baseurl + input

## Start program
 ##   try:
 ##       console.run()
  ##  except KeyboardInterrupt:
 ##       print('\nHuha!')