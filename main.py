import random
import sys

die = [1,2,3,4,5]

def play():
	for i in range(0,10):
		for j in range(0,5):
			die[j] = roll()
	if hasStraight():
		print("Straight!")

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


if len(sys.argv) != 2:
		print("Expected one argument, " + str(len(sys.argv)-1) + " arguments found.")
else:
	for j in range(0,int(sys.argv[1])):
		play()