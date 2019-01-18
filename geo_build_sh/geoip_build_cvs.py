#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import socket
import struct
import ipaddr
import csv
import netaddr
from os import path


def readCountryCode(geo_dir):
    geo_country_path = path.join(geo_dir, "GeoLite2-Country-Locations-en.csv")
    with open(geo_country_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        country_codes = {}
        for row in csv_reader:
            country_codes[row[0]] = {'code': row[4],
                                     'name': row[5]}

        return country_codes


def find_ip_segment(ip_str):
    addrs = netaddr.IPNetwork(ip_str)
    return addrs[0], addrs[-1]

def buildGeoIP(geo_dir, ip_block_file, save_name=None):
    if not save_name:
        save_name = "GeoIPCountryWhois.csv"

    countryCoders = readCountryCode(geo_dir)
    geo_ip_path = path.join(geo_dir, ip_block_file)
    with open(geo_ip_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_reader.next()
        geo_ip_save_path = path.join(geo_dir, save_name)
        with open(geo_ip_save_path, 'a') as save_csv:
            geo_ip_writer = csv.writer(save_csv, delimiter=',')
            for row in csv_reader:
                countryCode = row[1] if row[1] else row[2]
                if not countryCode:
                    continue
                countryInfo = countryCoders[countryCode]
                ip_start, ip_end = find_ip_segment(row[0])
                ip_start = str(ip_start)
                ip_end = str(ip_end)
                _geo_ip = [ip_start,
                           ip_end,
                           ip2int(ip_start),
                           ip2int(ip_end),
                           countryInfo["code"],
                           countryInfo["name"]]
                geo_ip_writer.writerow(_geo_ip)


def ip2int(addr):
    return int(ipaddr.IPAddress(addr))


def int2ip(addr):
    return socket.inet_ntoa(struct.pack("!I", addr))


def main():
    geo_dir = "GeoLite2-Country-CSV_20190115"
    save_name = "GeoIPCountryWhois.csv"
    # print(readCountryCode(geo_dir))
    save_file = path.join(geo_dir, save_name)
    os.remove(save_file)

    buildGeoIP(geo_dir, 'GeoLite2-Country-Blocks-IPv4.csv', save_name)
    # buildGeoIP(geo_dir, 'GeoLite2-Country-Blocks-IPv6.csv', save_name)


if __name__ == "__main__":
    main()
