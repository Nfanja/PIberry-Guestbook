#!/usr/bin/env python3

import sys
import io
import urllib.request
import argparse

def getGuestbook(url):
    return urllib.request.urlopen(url).read()


def main():
    parser = argparse.ArgumentParser(description="In general gets xml data by url. As second argument You can choose guestbook")
    parser.add_argument("url", nargs='?', help="url to get xml from", default=sys.stdin)
    parser.add_argument("-g", "--greeting", help="Greeting's ID", default="")
    args = parser.parse_args()
    
    if isinstance(args.url, io.TextIOWrapper):
        args.url = args.url.readline()

    args.url = args.url.rstrip()

    if args.url[-1] != "/":
        args.url = args.url + "/"

    if args.greeting:
        args.url += args.greeting + "/"

    return str(getGuestbook(args.url))[2:-1].replace('\\n', '')


if __name__ == '__main__':
    sys.stdout.write(main())
    sys.stderr.close()
