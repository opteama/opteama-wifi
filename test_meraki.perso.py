# -*- coding: utf-8 -*-
"""Test for Meraki class"""
__status__ = "Prototype"
__author__ = "guillain.sanchez@dimensiondata.com"

from meraki import Meraki
import sys, json

# Constantes for test and validation
token = 'c912f1ae714f1b013c1e20c8ab7c6a13ee84423c'
url = 'https://dashboard.meraki.com/api/v0'
organization_id = '709782'

building = 'SKP'
floor = '1c'
serial = 'Q2KD-8F7L-XRTA' # connected
name = 'TLS-AP-SKP-1c-3' # not used
site = 'TOULOUSE' #TLS
lat = '3.4743636'
lon = '40.3743194'

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

    # print("DELETE validation")
    # rjson = meraki.delete(
    #     serial = serial
    # )
    # if rjson in('', None):
    #     print('No data')
    # else:
    #     print(rjson)

if __name__ == '__main__':
    main()
