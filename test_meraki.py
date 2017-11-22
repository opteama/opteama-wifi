#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test for Meraki class"""
__status__ = "Prototype"
__author__ = "guillain.sanchez@dimensiondata.com"

from meraki import Meraki
import sys, json

# Constantes for test and validation
token = ''
url = 'https://dashboard.meraki.com/api/v0'
organization_id = ''

building = ''
floor = ''
serial = ''
name = ''
site = ''
lat = ''
lon = ''

def main():
    rjson = ""

    meraki = Meraki(
        token = token, 
        base_url = url,
        organization_id = organization_id
    )

    print("GET validation")
    rjson = meraki.get()
    if rjson in('', None):
        print('No data')
    else:
        print(rjson)

    print("GET validation - site")
    rjson = meraki.get(site = site)
    if rjson in('', None):
        print('No data')
    else:
        print(rjson)

    print("GET validation - site - serial")
    rjson = meraki.get(site = site, serial = serial)
    if rjson in('', None):
        print('No data')
    else:
        print(rjson)


    print("POST validation")
    rjson = meraki.post(
        building = building, 
        floor = floor,
        serial = serial,
        site = site,
        lat = lat,
        lon = lon
    )
    if rjson in('', None):
        print('No data')
    else:
        print(rjson)

    print("PUT validation")
    rjson = meraki.put(
        building = building,
        floor = floor,
        serial = serial,
        site = site,
        lat = lat,
        lon = lon
    )
    if rjson in('', None):
        print('No data')
    else:
        print(rjson)

    print("DELETE validation")
    rjson = meraki.delete(
        serial = serial
    )
    if rjson in('', None):
        print('No data')
    else:
        print(rjson)

if __name__ == '__main__':
    main()

