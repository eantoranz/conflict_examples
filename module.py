import sys

colors = {"black": "black mirror",
          "white": "white noise",
          "blue": "blue sky"}

def getFormattedPhrase(aColor):
    return "%s: %s" % (aColor, colors[aColor])

