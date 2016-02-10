import random

Graph = [[-1,-1,-1], [-1, -1, -1]]
Fail_score = 666

def Show_Graph():
	print "Now, the graph is: "
	for i in range(0, 2):
		for j in range(0, 3):
			if Graph[i][j] < 0:
				print '*',
			else:
				print Graph[i][j],
		print ""
	print " "

def One_turn():
	a = random.randint(1, 6)
	b = random.randint(1, 6)
	Show_Graph()
	print "Now, you get two numbers %d and %d" % (a, b)

	print "Please choose the position of number %d" % a
	position = int(raw_input("> "))
	while Graph[(position-1)/3][(position-1)%3] > 0:
		print "Please put the number in the right position"
		position = int(raw_input("> "))

	Graph[(position-1)/3][(position-1)%3] = a

	print "Please choose the position of number %d" % b
	position = int(raw_input("> "))
	while Graph[(position-1)/3][(position-1)%3] > 0:
		print "Please put the number in the right position"
		position = int(raw_input("> "))

	Graph[(position-1)/3][(position-1)%3] = b

def Cal_score():
	A_score = B_score = 0;
	for i in range(0, 3):
		A_score = A_score * 10 + (Graph[0][i])
		B_score = B_score * 10 + (Graph[1][i])

	if A_score < B_score:
		return Fail_score
	else:
		return A_score - B_score

def Start():
	for i in range(0, 2):
		for j in range(0, 3):
			Graph[i][j] = -1;
	for i in range(0, 3):
		One_turn()
	Score = Cal_score()
	print "Your score is ", Score
	print "\n"
	return Score

def New_game():
	print "Please enter the name of first player"
	Alice = raw_input("> ")

	print "Please enter the name of second player"
	Bob = raw_input("> ")
	Alice_score = 0
	Bob_score = 0

	for i in range(0, 10):
		Score = Start()
		if i & 1:
			Bob_score += Score
		else:
			Alice_score += Score 

	print "Game Over!!!"
	if Alice_score < Bob_score:
		print "The winner is %s" % (Alice)
	else:
		print "The winner is %s" % (Bob)

New_game()

