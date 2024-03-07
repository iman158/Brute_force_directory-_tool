#!/bin/python3

import requests
import argparse
import sys

# Argument parser setup
parser = argparse.ArgumentParser()
parser.add_argument('-w', '--wordlist', type=str, required=True, help="Switch for Wordlist")
parser.add_argument('-u', '--url', type=str, required=True, help="Switch for URL")
args = parser.parse_args()

# Displaying user inputs
print("[+] Wordlist: ", args.wordlist)
print("[+] URL: ", args.url)

# Request Headers
headers = {
    'User-Agent': 'Windows 10'
}

# Working with file
file = open(args.wordlist, 'r')
lines = file.readlines()

# Checking if URL schema exists in the url
if ('http' in args.url) or ('https' in args.url):
    pass
else:
    print('Please enter a URL Schema (http or https)')
    sys.exit()

# Parsing through each word in the wordlist
try:
    for line in lines:
        line = line.strip("\n")
        url_to_check = args.url + '/' + line
        response = requests.get(url_to_check, headers=headers)

        if response.status_code != 404:
            print(f"{url_to_check} : {response.status_code}")
except Exception as e:
    print("Error Occurred:", e)
