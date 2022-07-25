#!/usr/bin/python

import requests
import json
import argparse


def request_info(url):
		response = requests.get(url).text
		print(response)


parser = argparse.ArgumentParser()
parser.add_argument('-rdns', default=1, help='Lists Reverse DNS')
parser.add_argument('-iplookup', default=1, help='Lists GEO IP Location')
args = parser.parse_args()


target = input("Please Enter IP Address:")
print('\n')


print("Your Target IP address is {0}".format(target))
print('\n')




if args.rdns:
	target = args.rdns
	url = 'https://api.hackertarget.com/reversedns/?q=' + target
	print('Reverse DNS Information:')
	request_info(url)
	

if args.iplookup:
	target = args.iplookup
	url = 'https://api.hackertarget.com/geoip/?q=' + target
	print('GEOIP Information:')
	print('\n')
	request_info(url)


