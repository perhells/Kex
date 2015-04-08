import random
import sys

dice = [1,2,3,4,5]
smallCount = 0
largeCount = 0
threeCount = 0
fourCount = 0
yahtzeeCount = 0
fullCount = 0
totalScore = 0
bonusCount = 0
totalWithBonus = 0
totalWithoutBonus = 0
numberScore = 0

def play():
	score = 0
	currentRound = 0
	bonusScore = 0
	global usedCombinations
	global smallCount
	global largeCount
	global threeCount
	global fourCount
	global yahtzeeCount
	global fullCount
	global totalScore
	global totalWithBonus
	global totalWithoutBonus
	global numberScore
	global bonusCount
	usedCombinations =[False,False,False,False,False,False,False,False,False,False,False,False,False]
	# 0: Aces
	# 1: Twos
	# 2: Threes
	# 3: Fours
	# 4: Fives
	# 5: Sixes
	# 6: Three of a kind
	# 7: Four of a kind
	# 8: Small straight
	# 9: Straight
	# 10: Full house
	# 11: Chance
	# 12: Yahtzee
	while False in usedCombinations:
		for j in range(0,5):
			dice[j] = roll()
		currentRound += 1
		print(dice)
		if not usedCombinations[12] and yahtzee():
			score += 50
			yahtzeeCount += 1
			usedCombinations[12] = True
			print("Yahtzee! (" + str(dice) + " " + str(yahtzeeCount) + " out of " + str(currentRound) + " " + str(float(yahtzeeCount)/float(currentRound)) + ")")
		elif not usedCombinations[10] and fullHouse():
			score += 25
			fullCount += 1
			usedCombinations[10] = True
			print("Full House! (" + str(dice) + " " + str(fullCount) + " out of " + str(currentRound) + " " + str(float(fullCount)/float(currentRound)) + ")")
		elif not usedCombinations[7] and fourOfAKind():
			score += sum(dice)
			fourCount += 1
			usedCombinations[7] = True
			print("Four of a Kind! (" + str(dice) + " " + str(fourCount) + " out of " + str(currentRound) + " " + str(float(fourCount)/float(currentRound)) + ")")
		elif not usedCombinations[6] and threeOfAKind():
			score += sum(dice)
			threeCount += 1
			usedCombinations[6] = True
			print("Three of a Kind! (" + str(dice) + " " + str(threeCount) + " out of " + str(currentRound) + " " + str(float(threeCount)/float(currentRound)) + ")")
		elif not usedCombinations[9] and straight():
			score += 40
			largeCount += 1
			usedCombinations[9] = True
			print("Straight! (" + str(dice) + " " + str(largeCount) + " out of " + str(currentRound) + " " + str(float(largeCount)/float(currentRound)) + ")")
		elif not usedCombinations[8] and smallStraight():
			score += 30
			smallCount += 1
			usedCombinations[8] = True
			print("Small Straight! (" + str(dice) + " " + str(smallCount) + " out of " + str(currentRound) + " " + str(float(smallCount)/float(currentRound)) + ")")
		else:
			print("JA")
			maxCount = 0
			number = 0
			for i in range(1,7):
				if not usedCombinations[i-1]:
					tempCount = 0
					for die in dice:
						if die == i:
							tempCount += 1
					if tempCount >= maxCount:
						maxCount = tempCount
						number = i
						print("DERP: " +str(number) + " : " + str(maxCount) + " -> " + str(usedCombinations[number-1]))
			if number > 0:
				usedCombinations[number-1] = True
				print(str(number) + " had score " + str(score))
				for die in dice:
					if die == number:
						score += die
						bonusScore += die
				print(str(number) + " gave score " + str(score))
			else:
				if not usedCombinations[11]:
					usedCombinations[11] = True
					score += sum(dice)
				else:
					print(str(number) + " <- wtf")
					for i in range(0,len(usedCombinations)):
						if usedCombinations[i] == False:
							usedCombinations[i] = True
							break
	if bonusScore >= 63:
		bonusCount += 1
		score += 35
		totalWithBonus += score
		print("Score: " + str(score) + " (BONUS!)")
	else:
		totalWithoutBonus += score
		print("Score: " + str(score) + " (no bonus... bonus score: " + str(bonusScore) + ")")
	numberScore += bonusScore
	totalScore += score


def roll():
	return random.randrange(1,7)

def straight():
	# There are 5! ways of rolling each of the large straights.
	# This gives it a probability of 2*5!/6^5 = 240/7776 ≃ 0.031 on the first roll.
	return 	1 in dice and \
			2 in dice and \
			3 in dice and \
			4 in dice and \
			5 in dice\
			or \
			2 in dice and \
			3 in dice and \
			4 in dice and \
			5 in dice and \
			6 in dice

def smallStraight():
	# ~21% chance on the first roll
	# ~15% ?
	return 	1 in dice and \
			2 in dice and \
			3 in dice and \
			4 in dice\
			or \
			2 in dice and \
			3 in dice and \
			4 in dice and \
			5 in dice\
			or \
			3 in dice and \
			4 in dice and \
			5 in dice and \
			6 in dice 

def yahtzee():
	# 6/7776
	for i in range(1,7):
		yeah = True
		for die in dice:
			if die != i:
				yeah = False
		if yeah:
			return True
	return False

def fourOfAKind():
	# 6*5*5/7776 = 150/7776 ~= 0.0193
	# (Yahtzee excluded)
	for i in range(1,7):
		count = 0
		for die in dice:
			if die == i:
				count += 1
		if count >= 4: 
			return True
	return False


def threeOfAKind():
	# 6*10*25/7776 = 1500/7776 ~= 0.193
	# (Yahtzee excluded)
	for i in range(1,7):
		count = 0
		for die in dice:
			if die == i:
				count += 1
		if count >= 3: 
			return True
	return False

def fullHouse():
	# 1500*1/5/7776 = 300/7776 ~= 0.03858
	for i in range(1,7):
		for j in range(i,7):
			iCount = 0
			jCount = 0
			for die in dice:
				if die == i:
					iCount += 1
				elif die == j:
					jCount += 1
			if iCount >= 2 and jCount >= 2 and iCount+jCount == 5:
				return True
	return False

if len(sys.argv) != 2:
		print("Expected one argument, " + str(len(sys.argv)-1) + " arguments found.")
else:
	for j in range(1,int(sys.argv[1])+1):
		play()
	print("Average score: " + str(totalScore/int(sys.argv[1])))
	print("Bonus count: " + str(bonusCount) + " (Average score " + str(totalWithBonus/int(sys.argv[1])) + ")")
	print("Bonus missing count: " + str(int(sys.argv[1])-bonusCount) + " (Average score " + str(totalWithoutBonus/int(sys.argv[1])) + ")")
	print("Number score: " + str(numberScore/int(sys.argv[1])))