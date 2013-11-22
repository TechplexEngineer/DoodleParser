#!/usr/bin/python

link = 'http://doodle.com/cqhcwph947kpmficm8inbyyt/admin?#table'

import smtplib
from urllib import urlopen
import re

fromaddr = 'From Address'
toaddrs  = 'To Address'

# Add the From: and To: headers at the start!
msg = ("From: %s\r\nTo: %s\r\nSubject: Home Temp Status\r\n\r\n"
	% (fromaddr, toaddrs))

temp = urlopen("http://www.eece.maine.edu/cgi-bin/test-cgi").read()
pat=re.compile(r'^REMOTE_HOST = (.*)$',re.MULTILINE)
match=re.search(pat,temp)
host=match.group(1)
host='Link to automation system status\r\nhttp://' + host + '/cgi-bin/temp.pl'
msg=msg+host
server = smtplib.SMTP('outgoing.gwi.net')
server.login('Username','Password')
#server.set_debuglevel(1)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()