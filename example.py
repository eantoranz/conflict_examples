#!/usr/bin/python

import sys

colors = {"black": "black mirror",
          "white": "white noise",
          "blue": "blue sky"}

def getPhrase(color):
    if color not in colors:
        sys.stderr.write("Phrase for color %s is not defined\n" % color)
        sys.exit(1)
    phrase = getFormattedPhrase(color)
    return phrase

def getFormattedPhrase(aColor):
    return "%s: %s" % (aColor, colors[aColor])

print(getPhrase(sys.argv[1]))
