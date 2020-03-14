#!/usr/bin/python

import sys

colors = {"black": "black mirror",
          "white": "white noise",
          "green": "green peas",
          "blue": "blue sky"}

def getPhrase(color):
    phrase = colors[color]
    return phrase

print(getPhrase(sys.argv[1]))
