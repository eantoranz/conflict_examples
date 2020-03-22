#!/usr/bin/python

import sys

colors = {"black": "black mirror",
          "white": "white noise",
          "blue": "blue sky"}

def getPhrase(color):
    phrase = getFormattedPhrase(color)
    return phrase

def getFormattedPhrase(aColor):
    return "%s: %s" % (aColor, colors[aColor])

print(getPhrase(sys.argv[1]))
