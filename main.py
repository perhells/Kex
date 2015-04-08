import random
import sys

die = [1,2,3,4,5]
smallCount = 0
largeCount = 0

def play(count):
	global smallCount
	global largeCount
	for i in range(0,10):
		for j in range(0,5):
			die[j] = roll()
	if hasStraight():
		largeCount += 1
		print("Straight! (" + str(die) + " " + str(largeCount) + " out of " + str(count) + " " + str(float(largeCount)/float(count)) + ")")
	elif hasSmallStraight():
		smallCount += 1
		print("Small Straight! (" + str(die) + " " + str(smallCount) + " out of " + str(count) + " " + str(float(smallCount)/float(count)) + ")")


def roll():
	return random.randrange(1,7)

def hasStraight():
	# There are 5! ways of rolling each of the large straights.
	# This gives it a probability of 2*5!/6^5 = 240/7776 ≃ 0.031 on the first roll.
	return 	1 in die and \
			2 in die and \
			3 in die and \
			4 in die and \
			5 in die\
			or \
			2 in die and \
			3 in die and \
			4 in die and \
			5 in die and \
			6 in die

def hasSmallStraight():
	# ~21% chance on the first roll
	return 	1 in die and \
			2 in die and \
			3 in die and \
			4 in die\
			or \
			2 in die and \
			3 in die and \
			4 in die and \
			5 in die\
			or \
			3 in die and \
			4 in die and \
			5 in die and \
			6 in die 


# for j in range(0,1000):
# 	for i in range(0,5):
# 		die[i] = roll()

# 	if hasStraight():
# 		largeCount += 1
# 	if hasSmallStraight():
# 		smallCount += 1

# print("Straight! (" + str(die) + " " + str(largeCount) + " out of " + str(j) + " " + str(float(largeCount)/float(j)) + ")")
# print("Small Straight! (" + str(die) + " " + str(smallCount) + " out of " + str(j) + " " + str(float(smallCount)/float(j)) + ")")


if len(sys.argv) != 2:
		print("Expected one argument, " + str(len(sys.argv)-1) + " arguments found.")
else:
	for j in range(1,int(sys.argv[1])+1):
		play(j)