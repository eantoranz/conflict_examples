#!/usr/bin/python

import sys

colors = {"black": "black mirror",
          "green": "green peas",
          "white": "white noise",
          "blue": "blue sky"}

def getPhrase(color):
    phrase = colors[color]
    return phrase

print(getPhrase(sys.argv[1]))
