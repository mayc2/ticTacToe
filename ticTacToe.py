#!/bin/python

import random

class game(object):
	def __init__(self):
		super(game,self).__init__()
		self.rows = [['-','-','-'],['-','-','-'],['-','-','-']]
		self.rowValues = {1:'A',2:'B',3:'C'}
		self.rowCount = {'A':0,'B':1,'C':2}
		self.turn = "1"

	def getRowValue(self,index):
		return self.rowValues[index]

	def printBoard(self):
		print "    0 1 2 "
		print "   ------- "
		count = 1 
		for row in self.rows:
			output = self.rowValues[count]
			output +=  " | "
			for column in row:
				output += column + " "
			output += "|"
			print output
			count += 1
		print "   ------- "

	def opponentsTurn(self):
		if self.turn == "2":
			return True
		return False

	def rowComplete(self,index):
		for place in self.rows[index]:
			if place == '-':
				return False
		return True

	def allRowsComplete(self):
		for i in [0,1,2]:
			if self.rowComplete(i) == False:
				return False
		return True

	def columnComplete(self,index):
		for row in self.rows:
			if row[index] == '-':
				return False
		return True

	def allColumnsComplete(self):
		for i in [0,1,2]:
			if self.columnComplete(i) == False:
				return False
		return True

	def upRightComplete(self):
		if self.rows[2][0] == "-":
			return False
		if self.rows[1][1] == "-":
			return False
		if self.rows[0][2] == "-":
			return False
		return True

	def downRightComplete(self):
		if self.rows[0][0] == "-":
			return False
		if self.rows[1][1] == "-":
			return False
		if self.rows[2][2] == "-":
			return False	
		return True	


	def winner(self):
		#handle rows
		index = 0
		for row in self.rows:
			if self.rowComplete(index) and row[0] == row[1] and row[1] == row [2]:
				print "\nPlayer " + self.turn + " loses.\n\n"
				return 1
			index += 1

		#handle columns
		index = 0
		for column in [0,1,2]:
			if self.columnComplete(index) and self.rows[0][column] == self.rows[1][column] and self.rows[1][column] == self.rows[2][column]:
				print "\nPlayer " + self.turn + " loses.\n\n"
				return 1
			index += 1

		#handle diagonals
		if self.downRightComplete() and self.rows[0][0] == self.rows[1][1] and self.rows[1][1] == self.rows[2][2]:
			print "\nPlayer " + self.turn + " loses.\n\n"
			return 1
		if self.upRightComplete() and self.rows[2][0] == self.rows[1][1] and self.rows[1][1] == self.rows[0][2]:
			print "\nPlayer " + self.turn + " loses.\n\n"
			return 1
					
		if self.allRowsComplete() and self.allColumnsComplete() and self.upRightComplete() and self.downRightComplete():
			print "\nNo Winner.\n\n"
			return 1

		return 0

	def validateMove(self,location):
		if (location[0] in ['A','B','C']) and (location[1] in ['0','1','2']):
			if self.rows[self.rowCount[location[0]]][int(location[1])] == "-":
				return True
		return False

	def move(self):
		loc = raw_input("\nPlayer " + self.turn + " please make a move. (i.e A,1)\n")
		location = loc.split(",")
		if self.validateMove(location) == False:
			print "\n\nInvald move."
		else:
			if self.turn == "1":
				self.rows[self.rowCount[location[0]]][int(location[1])] = "X"
				self.turn = "2"
			else:
				self.rows[self.rowCount[location[0]]][int(location[1])] = "O"
				self.turn = "1"

	def moveOpponent(self, location):
		print "\nPlayer 2 has moved."
		self.rows[self.rowCount[location[0]]][int(location[1])] = "O"
		self.turn = "1"		

class player(object):
	def __init__(self):
		super(player,self)

	def selectMove(self,board):
		testColumn = random.randint(0,2)
		testRow = board.getRowValue(random.randint(1,3))
		temp = [testRow, str(testColumn)]
		if board.validateMove(temp) != True:
			temp = self.selectMove(board)
		return temp

def requestPlayers():
	temp = 0
	while temp not in (1,2):
		temp = int(raw_input("How many players (Options: 1,2)? "))
	return temp

def main():
	num_players = requestPlayers()
	board = game()
	board.printBoard()
	
	#single player
	if num_players == 1:
		oponent = player()
		while(board.winner() == 0):
			if board.opponentsTurn():
				move = oponent.selectMove(board)
				board.moveOpponent(move)
			else:
				board.move()
			board.printBoard()

	#multiplayer
	if num_players == 2:
		while(board.winner() == 0):
			board.move()
			board.printBoard()
	
	return 0


if __name__ == '__main__':
	main()