#!/usr/bin/python

import sys

RESET=chr(0x1b) + "[m"
colors = {"black": {"phrase": "black mirror", "fg": chr(0x1b) + "[0;7m"}, # reverse on color
          "white": {"phrase": "white noise", "fg": chr(0x1b) + "[1m"},
          "blue": {"phrase": "blue sky", "fg": chr(0x1b) + "[1;34m"}}

def getPhrase(color, useColor):
    """
    Get the phrase that corresponds to one color
    
    Parameters
    ----------
    color: color to get the phrase for. It can be used in any combination of uppercase/lowercase letters
    useColor: we can change the color of the phrase when writing on the output
    """
    color = color.lower()
    if color not in colors:
        sys.stderr.write("There is no phrase defined for color %s\n" % color)
        sys.exit(1)
    phrase = colors[color]["phrase"]
    if useColor:
        phrase = colors[color]["fg"] + ("%s: %s" % (color, phrase)) + RESET
    return phrase

for color in sys.argv[1:]:
    print(getPhrase(color, True))
