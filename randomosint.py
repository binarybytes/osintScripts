#!/usr/bin/python

import os
import sys
import json
import hashlib
import argparse
import re
import socket
import requests
import time

#check MS only
if(os.name == 'nt') or (sysplatform == "win32"): 
	os.system("")  #enable ansi color

#color
color = {
	"purple": "\033[5;95m",
	"cyan": "\033[5;96m",
	"red": "\033[0;31m",
	"clear": "\033[0m",
}

#start
if __name__ == "__main__":

#create request fields
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

print(color["purple"],"Please enter the IP Address:", color["clear"])
target_ip = input()

print(color["cyan"], 'This program captures: GeoIP, nmap, grabs HTTP Headers, and reverse DNS for an IP address',color["clear"])
print(color["purple"],'Quick Hacker Target Script', color["clear"])
print('\n')
print(color["cyan"], 'Your Target IP address is {0}'.format(target_ip), color["clear"])
print('\n')


#Get IP To SCAN
print(color["cyan"], 'Would you like target info about {0}? (Y/N):'.format(target_ip), color["clear"])

resp = input()

if resp.lower() in ["yes", "y"]:
        target = target_ip
else:
        target = input(prCyan("What IP would you like to check?: "))

print('\n')

def loading():
    print("Loading...")
    for i in range(0, 100):
        time.sleep(0.1)
        sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "%")
        sys.stdout.flush()
    return loading()

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
	
print(color["cyan"],('Reverse DNS Information:'))
print(color["purple"],(args.rdns))
print('\n')
print(color["purple"],('GEOIP Information:'))
print(color["cyan"],(args.iplookup))
print('\n')
print(color["cyan"],('NMAP of Traget (Only Ports: 21,25,80 and 443):'))
print(color["purple"],(args.nmap))
print('\n')
print(color["cyan"],('HTTP Headers:'))
print(color["purple"],(args.header))
print('\n')
print(color["cyan"],('HTTP Headers:'))
print(color["purple"],(args.header), color["clear"])
print('\n')

exit = input()
