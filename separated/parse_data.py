#!/usr/bin/env python3

import sys
import io
import argparse

import xml.etree.ElementTree as EL

def parseGreeting(data):
    return data.find('content').text


def parseGuestbook(data):
    guestbook_text = ""
    for greeting in data:
        guestbook_text += parseGreeting(greeting) + "\n"

    return guestbook_text


def main():
    parser = argparse.ArgumentParser(description="Parses guestbook data")
    parser.add_argument("data", nargs='?', help="String with guestbook or greeting data in xml", default=sys.stdin)
    parser.add_argument("-g", "--greeting", help="Indicates if passed data is greeting", action="store_true")
    args = parser.parse_args()

    if isinstance(args.data, io.TextIOWrapper):
        args.data = args.data.readline()

    root = EL.fromstring(args.data)

    if (args.greeting):
        return parseGreeting(root)
    else:
        return parseGuestbook(root)


if __name__ == '__main__':
    sys.stdout.write(main())
