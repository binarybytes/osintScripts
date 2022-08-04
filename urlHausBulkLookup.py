#!/usr/bin/python3

#updated urlhaus script
#removed urllib3 library (http connection pool + encode/decode)
#added requests

import sys
import requests
import json
import os


def query_urlhaus(url):
    data = {'url' : url}
    response = requests.post('https://urlhaus-api.abuse.ch/v1/url/', data)
    json_response = response.json()
    if json_response['query_status'] == 'ok':
        print(f"[+] FOUND:     {url}")
    elif json_response['query_status'] == 'no_results':
        print(f"[-] Not found: {url}")
    else:
        print(f"[-] Error:     {url}")

if len(sys.argv) > 1:
    if not os.path.isfile(sys.argv[1]):
        print("Input file not found")
        quit()
    file = open(sys.argv[1], 'r')
    urls = file.readlines()
    for url in urls:
        query_urlhaus(url.strip())
else:
    print("Takes a local file name as argument and looks up each URL sequentialy on the URLhaus bulk API")
    print("Input file must contain one URL per line")
    print("Usage: python3 lookup_url_bulk.py <input file>")
