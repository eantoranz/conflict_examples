#!/usr/bin/python

import sys

colors = {"black": "black mirror",
          "white": "white noise",
          "blue": "blue sky"}

def getPhrase(origColor):
    color = origColor.lower()
    if color not in colors:
        sys.stderr.write("There is no phrase defined for color %s\n" % origColor)
        sys.exit(1)
    phrase = colors[color]
    phrase = "Color: %s\nPhrase: %s" % (origColor, phrase)
    return phrase

print(getPhrase(sys.argv[1]))
