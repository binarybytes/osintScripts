#!/usr/bin/python

import os
import sys
import json
import hashlib
import argparse
import re
import socket
import requests

os.system('')
if(os.name == 'nt') or (sysplatform == "win32"): # msonly
    from ctypes import windll
    k = windll.kernel32
    k.SetConsoleMode(k.GetStdHandle(-11), 7)




#start

if __name__ == "__main__":




	def request_info(url):
		request = requests.get(url).json()
		response = request.text
		print(response)
	parser = argparse.ArgumentParser()
	parser.add_argument("-d","--dns", help="Find DNS records for a domain, results are determined using the dig DNS tool.")
	parser.add_argument("-rd","--rdns", help="Find Reverse DNS records for an IP address or a range of IP addresses.")
	parser.add_argument("-dhost","--dns_host", help="Find forward DNS (A) records for a domain.")
	parser.add_argument("-sdns","--shared", help="Find hosts sharing DNS servers.")
	parser.add_argument("-z","--zone", help="Online Test of a zone transfer that will attempt to get all DNS records for a target domain")
	parser.add_argument("-w","--whois", help="Determine the registered owner of a domain or IP address block with the whois tool.")
	parser.add_argument("-i","--iplookup", help="Find the location of an IP address using the GeoIP lookup location tool.")
	parser.add_argument("-r","--rip", help="Discover web hosts sharing an IP address with a reverse IP lookup.")
	parser.add_argument("-tcp","--tcp_port", help="Determine the status of an Internet facing service or firewall")
	parser.add_argument("-udp","--udp_port", help="Online UDP port scan available for common UDP services")
	parser.add_argument("-s","--sub_look", help="Determine the properties of a network subnet")
	parser.add_argument("-http","--header", help="View HTTP Headers of a web site. The HTTP Headers reveal system and web application details.")
	parser.add_argument("-e","--extract", help="Dump all the links from a web page.")
	parser.add_argument("-n","--nmap", help="Run a quick nmap scan from hackertarget")
	args = parser.parse_args()

	my_ip = input("Enter the IP Address:")

	print(cyan('Get Reverse DNS, GeoIP, NMAP, Traceroute and pulls HTTP Headers for an IP address'))
	print(cyan('quick hacker target script'))
	print('\n')
	print(cyan('Your Target IP address is {0}'.format(my_ip)))
	print('\n')


    #Get IP To SCAN

resp = input(cyan('Would you like target info about {0}? (Y/N):'.format(my_ip)))

if resp.lower() in ["yes", "y"]:
        badip = my_ip
else:
        badip = input(prCyan("What IP would you like to check?: "))

print('\n')


    #IP INFO
if args.dns:
	target = args.dns
	url = "https://api.hackertarget.com/dnslookup/?q=" + target
	request_info(url)
if args.rdns:
	target = args.rdns
	url = "https://api.hackertarget.com/reversedns/?q=" + target
	request_info(url)
if args.dns_host:
	target = args.dns_host
	url = "https://api.hackertarget.com/hostsearch/?q=" + target
	request_info(url)
if args.shared:
	target = args.shared
	url = "https://api.hackertarget.com/findshareddns/?q=" + target
	request_info(url)
if args.zone:
	target = args.zone
	url = "https://api.hackertarget.com/zonetransfer/?q=" + target
	request_info(url)
if args.iplookup:
	target = args.iplookup
	url = "https://api.hackertarget.com/geoip/?q=" + target
	request_info(url)
if args.rip:
	target = args.rip
	url = "https://api.hackertarget.com/reverseiplookup/?q=" + target
	request_info(url)
if args.tcp_port:
	target = args.tcp_port
	url = "https://api.hackertarget.com/nmap/?q=" + target
	request_info(url)
if args.udp_port:
	target = args.udp_port
	url = "https://api.hackertarget.com/nmap/?q=" + target
	request_info(url)
if args.sub_look:
	target = args.sub_look
	url = "https://api.hackertarget.com/subnetcalc/?q=" + target
	request_info(url)
if args.header:
	target = args.header
	url = "https://api.hackertarget.com/httpheaders/?q=" + target
	request_info(url)
if args.extract:
	target = args.extract
	url = "https://api.hackertarget.com/pagelinks/?q=" + target
	request_info(url)
if args.nmap:
	target = args.nmap
	url = "https://api.hackertarget.com/nmap/?q=" + target
	request_info(url)
	
print(red('Reverse DNS Information:'))
print(blue(args.rdns))
print('\n')
print(red('GEOIP Information:'))
print(blue(args.iplookup))
print('\n')
print(red('NMAP of Traget (Only Ports: 21,25,80 and 443):'))
print(blue(args.nmap))
print('\n')
print(red('HTTP Headers:'))
print(blue(args.header))
print('\n')
print(red('HTTP Headers:'))
print(blue(args.header))
print('\n')
