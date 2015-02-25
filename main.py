#!/usr/bin/env python

__author__ = 'NegatioN'


import parse_site

baseurl = "http://www.nyaa.se/?page=search&term="


input = "sengoku"
parse_site.test(baseurl, input)

url = baseurl + input