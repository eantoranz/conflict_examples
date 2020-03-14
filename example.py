#!/usr/bin/python

import sys

colors = {"black": "black mirror",
          "white": "white noise",
          "red": "red tide",
          "blue": "blue sky"}

def getPhrase(color):
    phrase = colors[color]
    return phrase

print(getPhrase(sys.argv[1]))
