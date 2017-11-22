#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Meraki class to drive AP deployment"""
__status__ = "Prototype"
__author__ = "guillain.sanchez@dimensiondata.com"

import sys, requests, json

class Meraki:
    """
    Class for simple Meraki object to provide easy method
    """

    def __init__(self, token, base_url, organization_id):
        self.token = token
        self.base_url = base_url
        self.organization_id = organization_id

    def __repr__(self):
        return "{} - {} - {}".format(
            self.token, self.url, self.organization_id
        )

    # API features
    def get(self, site = None, serial = None):
        if site not in ('', None):
            if serial not in ('', None):
                return self.request("GET", "/networks/{}/devices/{}".format(self.get_networkId(site), serial), "")
            return self.request("GET", "/networks/{}/devices".format(self.get_networkId(site)), "")

        return self.request("GET", "/organizations/{}/inventory".format(self.organization_id), "")

    def post(self, serial, site, building, floor, lat = None, lon = None):
        index = 0

        name = "{}-AP-{}-{}-{}".format(site.upper(), building.upper(), floor, index)
        r = self.request(
            "POST", 
            "/networks/{}/devices/claim".format(self.organization_id),
            "Content-Disposition: form-data; name=\"serial\"\r\n\r\n" + serial + "\r\n")
        if r in ('', None):
            return

        r = self.put(serial, site, building, floor, lat, lon)
        return r

    def put(self, serial, site, building = None, floor = None, lat = None, lon = None):
        r = self.get(site = site, serial = serial)

        data = {}
        if lat not in ('', None):
            data['lat'] = lat
        if lon not in ('', None):
            data['lon'] = lon
        print(r['name'])

        name_arr = {}
        name_arr['site'], AP, name_arr['building'], name_arr['floor'], index = "{}".format(r['name']).split('-')

        if site not in ('', None):
            name_arr['site'] = site
        if building not in ('', None):
            name_arr['building'] = building
        if floor not in ('', None):
            name_arr['floor'] = floor

        data['name'] = '{}-AP-{}-{}-{}'.format(name_arr['site'], name_arr['building'], name_arr['floor'], index)

        r = self.request(
            "PUT",
            "/networks/{}/devices/{}".format(self.get_networkId(site), serial), 
            "Content-Disposition: form-data; {}".format(json.dumps(data)))
        return r

    def delete(self, serial):
        return 
        return self.request("POST", "/networks/{}/devices/{}/remove".format(self.organization_id, serial))

    # Functions
    def request(self, action, path, data):
        headers = {
            'x-cisco-meraki-api-key': self.token,
            'cache-control': "no-cache",
        }
        r = requests.request(action, self.base_url + path, headers=headers, data=data)
        if r.status_code != requests.codes.ok:
            return 'null'
        return r.json()

    def get_networkId(self, name):
        r = self.request("GET", "/organizations/{}/networks".format(self.organization_id), "")
        for rec in r:
            if rec['name'] == name:
                return rec['id']

    def get_network(self, name, id = None):
        r = self.request("GET", "/organizations/{}/networks".format(self.organization_id), "")
        for rec in r:
            if rec['name'] == name:
                if id not in ('', None):
                    return rec['id']
                return rec

    def get_organization(self, name, id = None):
        r = self.request("GET", "/organizations", "")
        for rec in r:
            if rec['name'] == name:
                if id not in ('', None):
                    return rec['id']
                return rec

