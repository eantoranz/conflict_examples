#!/usr/bin/python

import sys

colors = {"black": "black mirror",
          "white":  "white noise",
          "blue": "blue sky"}

def getPhrase(color):
    if color not in colors:
        sys.stderr.write("Got no phrase for color %s\n" % color)
        sys.exit(1)
    phrase = colors[color]
    return phrase

print(getPhrase(sys.argv[1]))
