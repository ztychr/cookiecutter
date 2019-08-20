#!/usr/bin/python3

import sys
import requests
import argparse
from bs4 import BeautifulSoup
from tqdm import tqdm

def redText(string):
    return str(('\033[91m' + string + '\033[0m'))

def boldText(string):
    print('\033[1m' + str(string) + '\033[0m')

def Main():
    # initialize the parser
    parser = argparse.ArgumentParser(description='Fetch and analyse cookies from selected websites.')
    parser.add_argument("url", help="URL to fetch cookies from", type=str)
    parser.add_argument("-v", "--verbose", help="run program in verbose mode", action="store_true")
    args = parser.parse_args()

    cookie_list = []

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
        boldText('\n- Running program in verbose mode')
        boldText('\n- Fetching cookies and looking up discriptions...\n')

        for cookie in tqdm(cookies):

            w_request = requests.get('https://cookiepedia.co.uk/cookies/' + cookie.name)
            bs = BeautifulSoup(w_request.content, 'html.parser')

            cookie_list.append(redText('name: ') + str(cookie.name))
            cookie_list.append(redText('domain:') + str(cookie.domain))
            cookie_list.append(redText('path: ')  + str(cookie.path))
            cookie_list.append(redText('expires: ') + str(cookie.expires))
            cookie_list.append(redText('value: ') + str(cookie.value))
            cookie_list.append(redText('version: ') + str(cookie.version))
            cookie_list.append(redText('Cookpedia information: '))

            paragraphs = bs.findAll('p', limit = 6)

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

            cookie_list.append(redText('name: ') + str(cookie.name))
            info = redText('Cookiepedia information: ') + str(bs.find('p').text)

            cookie_list.append(info + '\n')

        print('\n')
        for i in cookie_list:
            print(i)

if __name__ == "__main__":
    Main()
