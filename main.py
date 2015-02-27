import random


def roll():
	return random.randrange(1,7)
for j in range(0,39000000):
	die = []
	for i in range(0,5):
		die.append(roll())
	print(die)

