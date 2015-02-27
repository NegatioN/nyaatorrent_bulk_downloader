#!/usr/bin/env python

__author__ = 'NegatioN'


import parse_site

baseurl = "http://www.nyaa.se/?page=search&cats=1_37&filter=0&term="


input = "sengoku"
parse_site.test(baseurl, input)

url = baseurl + input