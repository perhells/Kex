import os
import random
import sys
import subprocess

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
stats = [0] * 400
lowest = 375
highest = 0
highestScores = [0,0,0,0,0,0,0,0,0,0,0,0,0]
totalScores = [0,0,0,0,0,0,0,0,0,0,0,0,0]

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
	global stats
	global lowest
	global highest
	global highestScores
	global totalScores
	combinationScores = [0,0,0,0,0,0,0,0,0,0,0,0,0]
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

		for k in range(0,2):
			if not usedCombinations[9] and straight():
				break
			elif not usedCombinations[8] and smallStraight() or not usedCombinations[9] and smallStraight():
				for i in range(1,7):
					while dice.count(i) > 1:
						fixed = False
						for j in range(0,5):
							if dice[j] == i:
								dice[j] = roll()
								fixed = True
								break
						if not fixed:
							if sum(dice) == 16:
								for k in range(0,5):
									if dice[k] == 6:
										dice[k] = roll()
							else:
								for k in range(0,5):
									if dice[k] == 1:
										dice[k] = roll()
			else:
				maxCount = 0
				number = 0
				for i in range(1,7):
					if not usedCombinations[i-1]: # or not usedCombinations[6] or not usedCombinations[7] or not usedCombinations[10] or not usedCombinations[12]:
						tempCount = 0
						for die in dice:
							if die == i:
								tempCount += 1
						if tempCount >= maxCount:
							maxCount = tempCount
							number = i
							# print("DERP: " +str(number) + " : " + str(maxCount) + " -> " + str(usedCombinations[number-1]))
				if number > 0:
					for i in range(0,5):
						if dice[i] != number:
							dice[i] = roll()
				else:
					for i in range(0,5):
						dice[i] = roll()
		currentRound += 1
		# print(dice)
		if not usedCombinations[12] and yahtzee():
			if not usedCombinations[dice[0]-1] and dice[0] >= 6 and bonusScore + 25 < 63:
				usedCombinations[dice[0]-1] = True
				score += sum(dice)
				combinationScores[dice[0]-1] = sum(dice)
				# print("Bonus was: " + str(bonusScore))
				bonusScore += sum(dice)
				# print("Added: (Yahtzee) " + str(sum(dice)) + " " + str(dice[0]))
				# print("Bonus is: " + str(bonusScore))
			else:
				score += 50
				yahtzeeCount += 1
				usedCombinations[12] = True
				combinationScores[12] = 50
			# print("Yahtzee! (" + str(dice) + " " + str(yahtzeeCount) + " out of " + str(currentRound) + " " + str(float(yahtzeeCount)/float(currentRound)) + ")")
		elif not usedCombinations[10] and fullHouse():
			score += 25
			fullCount += 1
			usedCombinations[10] = True
			combinationScores[10] = 25
			# print("Full House! (" + str(dice) + " " + str(fullCount) + " out of " + str(currentRound) + " " + str(float(fullCount)/float(currentRound)) + ")")
		elif not usedCombinations[7] and fourOfAKind():

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
						# print("DERP: " +str(number) + " : " + str(maxCount) + " -> " + str(usedCombinations[number-1]))
			if number >= 6 and not usedCombinations[number-1] and bonusScore + 20 < 63:
				usedCombinations[number-1] = True
				# print("Bonus was: " + str(bonusScore))
				for die in dice:
					if die == number:
						combinationScores[number-1] += die
						score += die
						bonusScore += die
				# print("Added: (Four) " + str(number* dice.count(number)) + " " + str(number))
				# print("Bonus is: " + str(bonusScore))
			else:
				score += sum(dice)
				fourCount += 1
				usedCombinations[7] = True
				combinationScores[7] = sum(dice)
				# print("Four of a Kind! (" + str(dice) + " " + str(fourCount) + " out of " + str(currentRound) + " " + str(float(fourCount)/float(currentRound)) + ")")
		elif not usedCombinations[6] and threeOfAKind():
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
						# print("DERP: " +str(number) + " : " + str(maxCount) + " -> " + str(usedCombinations[number-1]))
			if number >= 6 and not usedCombinations[number-1] and bonusScore + 15 < 63:
				usedCombinations[number-1] = True
				# print("Bonus was: " + str(bonusScore))
				for die in dice:
					if die == number:
						combinationScores[number-1] += die
						score += die
						bonusScore += die
				# print("Added: (Three) " + str(number * dice.count(number)) + " " + str(number))
				# print("Bonus is: " + str(bonusScore))
			else:
				score += sum(dice)
				threeCount += 1
				usedCombinations[6] = True
				combinationScores[6] = sum(dice)
				# print("Three of a Kind! (" + str(dice) + " " + str(threeCount) + " out of " + str(currentRound) + " " + str(float(threeCount)/float(currentRound)) + ")")
		elif not usedCombinations[9] and straight():
			score += 40
			largeCount += 1
			usedCombinations[9] = True
			combinationScores[9] = 40
			# print("Straight! (" + str(dice) + " " + str(largeCount) + " out of " + str(currentRound) + " " + str(float(largeCount)/float(currentRound)) + ")")
		elif not usedCombinations[8] and smallStraight():
			score += 30
			smallCount += 1
			usedCombinations[8] = True
			combinationScores[8] = 30
			# print("Small Straight! (" + str(dice) + " " + str(smallCount) + " out of " + str(currentRound) + " " + str(float(smallCount)/float(currentRound)) + ")")
		else:
			# print("JA")
			maxCount = 0
			number = 0
			for i in range(1,7):
				if not usedCombinations[i-1]:
					tempCount = dice.count(i)
					if tempCount >= maxCount:
						maxCount = tempCount
						number = i
						# print("DERP: " +str(number) + " : " + str(maxCount) + " -> " + str(usedCombinations[number-1]))
			if number > 0:
				# print(str(number) + " had score " + str(score))
				if number >= 4 and bonusScore + number * dice.count(number) < 63:
					if dice.count(number) < 3 and not usedCombinations[0]:
						usedCombinations[0] = True
						score += 1 * dice.count(1)
						combinationScores[0] = 1 * dice.count(1)
						# print("Bonus was: " + str(bonusScore))
						bonusScore += 1 * dice.count(1)
						# print("Added: " + str(1 * dice.count(1)) + " " + str(1))
						# print("Bonus is: " + str(bonusScore))
					elif dice.count(number) < 3 and not usedCombinations[12]:
						usedCombinations[12] = True
					elif dice.count(number) < 3 and not usedCombinations[1]:
						usedCombinations[1] = True
						score += 2 * dice.count(2)
						combinationScores[1] = 2 * dice.count(2)
						# print("Bonus was: " + str(bonusScore))
						bonusScore += 2 * dice.count(2)
						# print("Added: " + str(2 * dice.count(2)) + " " + str(2))
						# print("Bonus is: " + str(bonusScore))
					else:
						usedCombinations[number-1] = True
						score += number * dice.count(number)
						combinationScores[number-1] = number * dice.count(number)
						# print("Bonus was: " + str(bonusScore))
						bonusScore += number * dice.count(number)
						# print("Added: " + str(number * dice.count(number)) + " " + str(number))
						# print("Bonus is: " + str(bonusScore))

				else:
					usedCombinations[number-1] = True
					score += number * dice.count(number)
					combinationScores[number-1] = number * dice.count(number)
					# print("Bonus was: " + str(bonusScore))
					bonusScore += number * dice.count(number)
					# print("Added: " + str(number * dice.count(number)) + " " + str(number))
					# print("Bonus is: " + str(bonusScore))
				# print(str(number) + " gave score " + str(score))
			else:
				if not usedCombinations[11]:
					if sum(dice) <= 10 and not usedCombinations[12]:
						usedCombinations[12] = True
					else:
						usedCombinations[11] = True
						combinationScores[11] = sum(dice)
						score += sum(dice)
				else:
					# print(str(number) + " <- wtf")
					vaskat = False
					if bonusScore < 63:
						for i in range(6,len(usedCombinations)):
							if usedCombinations[i] == False:
								usedCombinations[i] = True
								vaskat = True
								break
					if not vaskat:
						for i in range(0,len(usedCombinations)):
							if usedCombinations[i] == False:
								usedCombinations[i] = True
								vaskat = True
								break

	if bonusScore >= 63:
		bonusCount += 1
		score += 35
		totalWithBonus += score
		# print("Score: " + str(score) + " (BONUS!) " + str(combinationScores))
	else:
		totalWithoutBonus += score
		# print("Score: " + str(score) + " (no bonus... bonus score: " + str(bonusScore) + ") " + str(combinationScores))
	numberScore += bonusScore
	totalScore += score
	stats[score] += 1
	if score > highest:
		# if bonusScore >= 63:
		# 	print("Score: " + str(score) + " " + str(combinationScores) + " (Y) " + str(sum(combinationScores)) + " B: " + str(bonusScore))
		# else:
		# 	print("Score: " + str(score) + " " + str(combinationScores) + " (N) " + str(sum(combinationScores)) + " B: " + str(bonusScore))

		highest = score
		highestScores = combinationScores
	if score < lowest:
		# print("Low: " + str(score))
		lowest = score
	for i in range(0,len(combinationScores)):
		totalScores[i] += float(combinationScores[i])


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
	os.system('cls' if os.name == 'nt' else 'clear')
	os.system('setterm -cursor off')
	rows, columns = os.popen('stty size', 'r').read().split()
	nom = True
	# s = Sound() 
	# s.read('pacman_chomp.wav') 
	# s.play()
	#subprocess.call(["afplay", "pacman_chomp.wav"])
	# subprocess.call(["ffplay", "-nodisp", "-autoexit", "pacman_chomp.wav"])
	# os.system("start pacman_chomp.wav")
	for j in range(1,int(sys.argv[1])+1):
		if j%(int(sys.argv[1])/100) == 0:
			percentage = int(j/int(sys.argv[1])*100)
			sys.stdout.write('\r')
			sys.stdout.write(' [')
			for k in range (1, int((int(columns)-8)*percentage/100)):
				sys.stdout.write(' ')
			if nom:
				sys.stdout.write('C')
				nom = False
			else:
				sys.stdout.write('c')
				nom = True
			for k in range (int((int(columns)-8)*percentage/100), int(columns)-8):
				if k % 2 == 0:
					sys.stdout.write('·')
				else:
					sys.stdout.write(' ')
			sys.stdout.write('] ')

			sys.stdout.write(str(percentage) + "%")
		play()
	for i in range(0,len(totalScores)):
		totalScores[i] = float(totalScores[i])/float(int(sys.argv[1]))
	print("Total rounds: " + str(sys.argv[1]))
	print("Average score: " + str(totalScore/int(sys.argv[1])))
	print("Bonus percentage: " + str("%.3f" % (bonusCount/int(sys.argv[1])*100)) + "% (Average score " + str(float(bonusCount*35)/int(sys.argv[1])) + ")")
	# print("Average score without bonus: " + str(totalWithoutBonus/int(sys.argv[1])))
	# print("Bonus count: " + str(bonusCount) + " (Average score " + str(float(bonusCount*35)/int(sys.argv[1])) + ")")
	# print("Bonus missing count: " + str(int(sys.argv[1])-bonusCount) + " (Average score " + str(totalWithoutBonus/int(sys.argv[1])) + ")")
	print("Number score: " + str(numberScore/int(sys.argv[1])))
	print("Lowest: " + str(lowest) + " Highest: " + str(highest))

	print(str(highestScores))
	for i in range(1, lowest % 10):
		print("\t\t", end="")
	counter = 0
	percentile = [lowest,0,0,0,0,0,0,0,0,0,0]
	index = 1
	for i in range(lowest,highest+1):
		# print(str(i) + "\t" + str(stats[i]))
		if i%10 == 0:
			print()
			print(str(i) + ":" + str(stats[i]), end="")
		else:
			if len(str(stats[i-1])) < 4:
				print("\t\t" + str(i) + ":" + str(stats[i]), end="")
			else:
				print("\t" + str(i) + ":" + str(stats[i]), end="")
		counter += stats[i]
		if counter - int(sys.argv[1])/10 >= 0:
			percentile[index] = i
			counter -= int(sys.argv[1])/10
			index += 1
	print()
	print()
	print("1\t2\t3\t4\t5\t6\tThree\tFour\tSS\tLS\tFH\tCH\tY\tB\tA")
	for score in totalScores:
		print(str("%.3f" % score) + "\t", end="")
	print(str("%.3f" % (float(bonusCount*35)/int(sys.argv[1]))) + "\t", end="")
	print(str("%.3f" % (totalScore/int(sys.argv[1]))) + "\t", end="")
	print()
	print()
	print("0%\t10%\t20%\t30%\t40%\t50%\t60%\t70%\t80%\t90%\t100%")
	for score in percentile:
		print(str(score) + "\t", end="")
	print()
	os.system('setterm -cursor on')