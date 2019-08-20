#!/usr/bin/python3
import sys
import requests
import argparse
from bs4 import BeautifulSoup
from tqdm import tqdm

cyan = '\033[96m'
red = '\033[91m'
bold = '\033[1m'
end = '\033[0m'

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
        print(bold + '\n' + '- Running program in verbose mode' + end)
        print(bold + '\n' + '- Fetching cookies and looking up discriptions...\n' + end)

        for cookie in tqdm(cookies):

            w_request = requests.get('https://cookiepedia.co.uk/cookies/' + cookie.name)
            bs = BeautifulSoup(w_request.content, 'html.parser')

            name = red + 'name: ' + end + cyan + cookie.name + end
            domain = red + 'domain: ' + end + cyan + str(cookie.domain) + end
            path = red + 'path: ' + end + cyan + str(cookie.path) + end
            expire = red + 'expires: ' + end + cyan + str(cookie.expires) + end
            value = red + 'value: ' + end + cyan + str(cookie.value) + end
            version = red + 'version: ' + end + cyan + str(cookie.version) + end
            paragraphs = bs.findAll('p', limit = 6)

            cookie_list.append(name)
            cookie_list.append(domain)
            cookie_list.append(path)
            cookie_list.append(expire)
            cookie_list.append(value)
            cookie_list.append(version)
            cookie_list.append(red + '\nCookpedia information: ' + end)

            for p in paragraphs:
                cookie_list.append(cyan + p.getText() + end)

            cookie_list.append('\n')

        for i in cookie_list:
            print(i)

    else:
        print(bold + 'Fetching cookies and looking up discriptions...\n' + end)

        for cookie in tqdm(cookies):
            w_request = requests.get('https://cookiepedia.co.uk/cookies/' + cookie.name)
            bs = BeautifulSoup(w_request.content, 'html.parser')

            name = red + 'Name: ' + end + cyan + cookie.name + end
            info = red + 'Information: ' + end + cyan + str(bs.find('p').text) + end

            cookie_list.append(name)
            cookie_list.append(info + '\n')

        print('\n')
        for i in cookie_list:
            print(i)

if __name__ == "__main__":
    Main()

