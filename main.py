import random

die = [1,2,3,4,5]

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

count = 0
for j in range(0,390000):
	for i in range(0,5):
		die[i] = roll()

	if hasStraight():
		count += 1
		print("Straight! (" + str(die) + " " + str(count) + " out of " + str(j) + " " + str(float(count)/float(j)) + ")")