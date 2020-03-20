#!/usr/bin/python

from module import getFormattedPhrase
import sys

def getPhrase(color):
    phrase = getFormattedPhrase(color)
    return phrase

print(getPhrase(sys.argv[1]))
