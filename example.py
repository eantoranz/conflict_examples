#!/usr/bin/python

import sys

colors = {"black": "black mirror",
          "white": "white noise",
          "blue": "blue sky"}

def getPhrase(color):
    phrase = colors[color]
    phrase = "%s: %s" % (color, phrase)
    return phrase

print(getPhrase(sys.argv[1]))
