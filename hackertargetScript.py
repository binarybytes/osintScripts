#!/usr/bin/python


#-----------------author---------------#
#                                      #
#		binarybytes	       #
#				       #
#--------------------------------------#

import requests

def request_info(url):
		response = requests.get(url).text
		print(response)

target = input("Please Enter IP Address:")
print('\n')

print("Your Target IP address is {0}".format(target))
print('\n')

if target:
	url = 'https://api.hackertarget.com/reversedns/?q=' + target
	print('Reverse DNS Information:')
	request_info(url)
	print('\n')
	

if target:
	url = 'https://api.hackertarget.com/geoip/?q=' + target
	print('GEOIP Information:')
	request_info(url)
	print('\n')

if target:
	url = 'https://api.hackertarget.com/hostsearch/?q=' + target
	print('Host Search:')
	request_info(url)
	print('\n')

if target:
	url = 'https://api.hackertarget.com/findshareddns/?q=' + target
	print('Shared DNS Servers:')
	request_info(url)
	print('\n')

if target:
	url = 'https://api.hackertarget.com/zonetransfer/?q=' + target
	print('Zone Transfer:')
	request_info(url)
	print('\n')

if target:
	url = 'https://api.hackertarget.com/reverseiplookup/?q=' + target
	print('Reverse IP Lookup:')
	request_info(url)
	print('\n')

if target:
	url = 'https://api.hackertarget.com/subnetcalc/?q=' + target
	print('Subnet Lookup:')
	request_info(url)
	print('\n')

if target:
	url = 'https://api.hackertarget.com/httpheaders/?q=' + target
	print('HTTP Headers:')
	request_info(url)
	print('\n')

if target:
	url = 'https://api.hackertarget.com/pagelinks/?q=' + target
	print('Page Links:')
	request_info(url)
	print('\n')

if target:
	url = 'https://api.hackertarget.com/aslookup/?q=' + target
	print('AS Lookup:')
	request_info(url)
	print('\n')


if target:
	url = 'https://api.hackertarget.com/bannerlookup/?q=' + target
	print('Banner Lookup:')
	request_info(url)
	print('\n')
