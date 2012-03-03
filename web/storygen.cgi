#!/usr/bin/python
from random import choice
import plotpoints
print "Content-type: text/html\n\n"
print "<link rel=stylesheet href=\"story.css\" type=\"text/css\">"
print "<p>"
print "Write a" + choice(plotpoints.genre) + " story about " + choice(plotpoints.subject) + " set in " + choice(plotpoints.setting) + "."
print "</p>"

