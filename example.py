#!/usr/bin/python

import sys

colors = {"black": "black mirror",
          "white": "white noise",
          "blue": "blue sky"}

def getPhrase(color):
    color = color.lower()
    if color not in colors:
        sys.stderr.write("There is no phrase defined for color %s\n" % color)
        sys.exit(1)
    phrase = colors[color]
    phrase = "%s: %s" % (color, phrase)
    return phrase

# I love color white
print(getPhrase("white"))
for color in sys.argv[1:]:
    print(getPhrase(color))
