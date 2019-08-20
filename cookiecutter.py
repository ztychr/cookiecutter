#!/usr/bin/python3

import sys
import requests
import argparse
from bs4 import BeautifulSoup
from tqdm import tqdm


def Main():
    # initialize the parser
    parser = argparse.ArgumentParser(description='Fetch and analyse cookies from selected websites.')
    parser.add_argument("url", help="URL to fetch cookies from", type=str)
    parser.add_argument("-v", "--verbose", help="run program in verbose mode", action="store_true")
    args = parser.parse_args()

    cookie_list = []
    verbosity_list = []

    #  get cookies from positional argument url
    try:
        if "https://" in args.url:
            c_request = requests.get(args.url)
        else:
            c_request = requests.get('https://' + args.url)
    except:
        print('Invalid url. Please try again.')
        sys.exit(0)

    cookies = c_request.cookies

    if args.verbose:
        print('\033[1m' + '\n' + '- Running program in verbose mode' + '\033[0m')
        print('\033[1m' + '\n' + '- Fetching cookies and looking up discriptions...\n' + '\033[0m')

        for cookie in tqdm(cookies):

            w_request = requests.get('https://cookiepedia.co.uk/cookies/' + cookie.name)
            bs = BeautifulSoup(w_request.content, 'html.parser')

            name = '\033[91m' + 'name: ' + '\033[0m'  + cookie.name
            domain = '\033[91m' + 'domain: ' + '\033[0m'  + str(cookie.domain)
            path = '\033[91m' + 'path: ' + '\033[0m'  + str(cookie.path)
            expire = '\033[91m' + 'expires: ' + '\033[0m'  + str(cookie.expires)
            value = '\033[91m' + 'value: ' + '\033[0m'  + str(cookie.value)
            version = '\033[91m' + 'version: ' + '\033[0m'  + str(cookie.version)
            cookpedia = '\033[91m' + '\nCookpedia information: ' + '\033[0m'

            paragraphs = bs.findAll('p', limit = 6)

            cookie_list.append(name)
            cookie_list.append(domain)
            cookie_list.append(path)
            cookie_list.append(expire)
            cookie_list.append(value)
            cookie_list.append(version)
            cookie_list.append(cookpedia)

            for p in paragraphs:
                cookie_list.append(p.getText())

            cookie_list.append('\n')

        for i in cookie_list:
            print(i)

    else:
        print('\033[1m' + '\n' + '- Fetching cookies and looking up discriptions...\n' + '\033[0m')

        for cookie in tqdm(cookies):
            w_request = requests.get('https://cookiepedia.co.uk/cookies/' + cookie.name)
            bs = BeautifulSoup(w_request.content, 'html.parser')

            name = '\033[91m' + 'Name: ' + '\033[0m'  + cookie.name + '\033[0m'
            info = '\033[91m' + 'cookiepedia information: ' + '\033[0m'  + str(bs.find('p').text)

            cookie_list.append(name)
            cookie_list.append(info + '\n')

        print('\n')
        for i in cookie_list:
            print(i)

if __name__ == "__main__":
    Main()
