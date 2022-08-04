#!/usr/bin/python


#-----------------author---------------#
#                                      #
#		binarybytes	       #
#				       #
#--------------------------------------#

import requests
from datetime import datetime
import os
os.system("") 

g = "\033[1;32m"
c = "\033[1;96m"
e = "\033[0;0m"

def request_info(url):
		response = requests.get(url).text
		print(response)

target = input("Please Enter IP Address:")
print('\n')

print(c + "-" * 84)	
print('\n' * 2)
print(c + "  _   _            _               _____                    _        _    ____ ___ ")
print(c + " | | | | __ _  ___| | _____ _ __  |_   _|_ _ _ __ __ _  ___| |_     / \  |  _ \_ _|")
print(c + " | |_| |/ _` |/ __| |/ / _ \ '__|   | |/ _` | '__/ _` |/ _ \ __|   / _ \ | |_) | | ")
print(c + " |  _  | (_| | (__|   <  __/ |      | | (_| | | | (_| |  __/ |_   / ___ \|  __/| | ")
print(c + " |_| |_|\__,_|\___|_|\_\___|_|      |_|\__,_|_|  \__, |\___|\__| /_/   \_\_|  |___|")
print(c + "                                                 |___/                             ")
print('\n' * 2)
print(c  + "-" * 84 + e)
print('\n' * 3)
print(g  + "-" * 50)
print(g + "Your Target IP address is "+target)
print(g + "Time Started: "+str(datetime.now()))
print(g + "-" * 50) 
print('\n' * 3)


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


print(g + "-" * 50)
print(g + "Time Ended: "+str(datetime.now()))
print(g+ "-" * 50) 
