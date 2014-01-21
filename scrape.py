#!/usr/bin/python

link = 'http://doodle.com/cqhcwph947kpmfic#table'


from urllib import urlopen
import re


from ghost import Ghost
ghost = Ghost()

page, resources = ghost.open(link)
page, resources = ghost.wait_for_page_loaded()
result, resources = ghost.evaluate(
    "doodleJS.data.poll")

print page
# , resources


# temp = urlopen("http://www.eece.maine.edu/cgi-bin/test-cgi").read()

# pat=re.compile(r'^REMOTE_HOST = (.*)$',re.MULTILINE)
# match=re.search(pat,temp)
# host=match.group(1)
