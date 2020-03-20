import sys

colors = {"black": "black mirror",
          "white": "white noise",
          "blue": "blue sky"}

def getFormattedPhrase(aColor):
    if aColor not in colors:
        sys.stderr.write("Got no phrase for color %s\n" % aColor)
        sys.exit(1)
    return "%s: %s" % (aColor, colors[aColor])

