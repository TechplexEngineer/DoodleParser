#!/usr/bin/python

import csv
import numpy as np
import itertools

my_data = np.genfromtxt('DoodleFLLJudge.csv', delimiter=',', dtype=str)

def OK2Letter(lst):
	out = []
	letter = ord('A')  # this isn't all that robust (More than 26 options)
	for i in range(0, len(lst)):
		if lst[i] == "OK":
			out.append(chr(letter))
		letter += 1
	return out

class Response:
	def __init__(self, days): #,name
		self.days=days
		
		# print 'days',days
	def __str__(self):
		out = '('
		for day in self.days:
			out += day
			out += " + "
		out += ')'
		out = out.replace(' + )',')')
		
		return out
	def __mul__(self, other):
		lst = map(''.join, itertools.chain(itertools.product(self.days, other.days), itertools.product(other.days, self.days)))
		# print lst
		return Response(lst).simplify()

	def simplify(self):
		out = []
		for day in self.days:
			out.append("".join(sorted("".join(set(day)))))
		self.days = list(set(out))

		out = []
		for day1 in self.days:
			for day2 in self.days:
				for char in day1:
					if char in day2:
						break
				# if day1 in day2 and day1 != day2:
				out.append(day1)
		self.days = list(set(out))
		# print "o2", out
		return self
		# for i in range(len(self.days)):
		# 	day = self.days[i]
		# 	print 'day',day
		# 	day = "".join(set(day))
		# 	print 'day2',day
			
			# if len(day) > 1:




responses = [] # list of response objects
canNotAttend = []
# create respnse objects based on the csv data
for res in my_data[6:]:
	if 'OK' in res[1:]:
		responses.append(Response(OK2Letter(res[1:])))
	elif res[0] != 'Count':
		canNotAttend.append(res[0])


# print out the responses
# print 'Responses:'
# for resp in responses:
# 	print str(resp)
print 'Can Not Attend:'
for a in canNotAttend:
	print a
print '-'*15
out = responses[0]
for resp in responses[1:]:
	out *= resp
	# print 'out:',out
	# print resp

days = out.days
# print days
daysbylen = sorted(days, key=len)
print daysbylen, len(daysbylen)

# minlenday = out.days[0]
# for day in out.days[1:]:
# 	if len(day) < len(minlenday):
# 		minlen = day

# print minlenday









