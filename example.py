#!/usr/bin/python

import sys

colors = {"black": "black mirror",
          "white": "white noise",
          "blue": "blue sky"}

def getPhrase(color):
    phrase = colors[color]
    phrase = phrase.upper()
    return phrase

print(getPhrase(sys.argv[1]))
