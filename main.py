import random
import sys

die = [1,2,3,4,5]
smallCount = 0
largeCount = 0
threeCount = 0
fourCount = 0
yahtzeeCount = 0

def play(count):
	global smallCount
	global largeCount
	global threeCount
	global fourCount
	global yahtzeeCount
	for i in range(0,10):
		for j in range(0,5):
			die[j] = roll()
	if yahtzee():
		yahtzeeCount += 1
		print("Yahtzee! (" + str(die) + " " + str(yahtzeeCount) + " out of " + str(count) + " " + str(float(yahtzeeCount)/float(count)) + ")")
	if fourOfAKind():
		fourCount += 1
		print("Four of a Kind! (" + str(die) + " " + str(fourCount) + " out of " + str(count) + " " + str(float(fourCount)/float(count)) + ")")
	if threeOfAKind():
		threeCount += 1
		print("Three of a Kind! (" + str(die) + " " + str(threeCount) + " out of " + str(count) + " " + str(float(threeCount)/float(count)) + ")")
	if hasStraight():
		largeCount += 1
		print("Straight! (" + str(die) + " " + str(largeCount) + " out of " + str(count) + " " + str(float(largeCount)/float(count)) + ")")
	if hasSmallStraight():
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
	# ~15% ?
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

def yahtzee():
	# 6/7776
	for i in range(1,7):
		yeah = True
		for dice in die:
			if dice != i:
				yeah = False
		if yeah:
			return True
	return False

def fourOfAKind():
	# 6*5*5/7776 = 150/7776 ~= 0.0193
	for i in range(1,7):
		count = 0
		for dice in die:
			if dice == i:
				count += 1
		if count == 4: 
			return True
	return False


def threeOfAKind():
	# 6*10*25/7776 = 1500/7776 ~= 0.193
	for i in range(1,7):
		count = 0
		for dice in die:
			if dice == i:
				count += 1
		if count == 3: 
			return True
	return False

if len(sys.argv) != 2:
		print("Expected one argument, " + str(len(sys.argv)-1) + " arguments found.")
else:
	for j in range(1,int(sys.argv[1])+1):
		play(j)