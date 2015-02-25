#!/usr/bin/env python

__author__ = 'NegatioN'


import parse_site

baseurl = "http://www.nyaa.se/?page=search&cats=1_37&filter=0&term="
baseurl2 = "http://www.nyaa.se/?page=search&cats=1_38&filter=0&term="


input = "naruto"
parse_site.test(baseurl2, input)

url = baseurl + input