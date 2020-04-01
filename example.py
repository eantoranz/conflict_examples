#!/usr/bin/python

import sys

colors = {"black": "black mirror",
          "white":  "white noise",
          "blue": "blue sky"}

def getPhrase(color):
    """
    Get the phrase that corresponds to one color
    
    Parameters
    ----------
    color: color to get the phrase for. It can be used in any combination of uppercase/lowercase letters
    """
    color = color.lower()
    if color not in colors:
        sys.stderr.write("There is no phrase defined for color %s\n" % color)
        sys.exit(1)
    phrase = colors[color]
    phrase = "%s: %s" % (color, phrase)
    return phrase

for color in sys.argv[1:]:
    print(getPhrase(color))
