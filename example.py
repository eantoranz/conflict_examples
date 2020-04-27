#!/usr/bin/python

from module import getFormattedPhrase
from module import colors
import sys

def getPhrase(color):
    if color not in colors:
        sys.stderr.write("Got no phrase for color %s\n" % color)
        sys.exit(1)
    phrase = getFormattedPhrase(color)
    return phrase

print(getPhrase(sys.argv[1]))
