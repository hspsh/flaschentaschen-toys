#!/usr/bin/env python3
"""
Flaschentaschen Game of Life
"""


__author__ = "Marcin Jasiukowicz"
__version__ = "0.1.0"
__license__ = "MIT"

import flashentaschen
import time
from copy import deepcopy
from tkinter import *
from threading import Timer

class GameOfLife:
	def __init__(self, X, Y):
		self.width = X
		self.height = Y
		self.board = [[0 for y in range(Y)] for x in range(X)]

	def loop(self):
		next_frame = deepcopy(self.board)
	
		for i, x in enumerate(self.board):
			for j, y in enumerate(self.board[i]):
				neighbours = self.checkNeighbours(i, j)
				if self.board[i][j] == 1:
					if neighbours > 3:
						next_frame[i][j] = 0
					if(neighbours == 2):
						next_frame[i][j] = 1
					if(neighbours == 3):
						next_frame[i][j] = 1
					if neighbours < 2:
						next_frame[i][j] = 0	
				if self.board[i][j] == 0:
					if(neighbours == 3):
						next_frame[i][j] = 1

		self.board = next_frame
	
	def checkNeighbours(self, x, y):
		number = 0
		if(self.board[(x-1) % self.width][y] == 1):
			number += 1
		if(self.board[(x-1) % self.width][(y-1) % self.height] == 1):
			number += 1
		if(self.board[x][(y-1) % self.height] == 1):
			number += 1
		if(self.board[(x+1) % self.width][(y-1) % self.height] == 1):
			number += 1
		if(self.board[(x+1) % self.width][y] == 1):
			number += 1
		if(self.board[(x+1) % self.width][(y+1) % self.height] == 1):
			number += 1
		if(self.board[x][(y+1) % self.height] == 1):
			number += 1
		if(self.board[(x-1) % self.width][(y+1) % self.height] == 1):
			number += 1
		return number

	def drawTo(self, canvas):
		self.loop()
		canvas.clear()
		for i, x in enumerate(self.board):
			for j, y in enumerate(self.board[i]):
				if self.board[i][j] == 1:
					canvas.point([i,j])

	def addGlider(self, X=0, Y=0):
		#     1
		# 1   1
		#   1 1
		glider = [
				[0, 1, 0],
				[0, 0, 1],
				[1, 1, 1]]
		
		self.drawShape(glider, X, Y)

	def addPenta(self, X=0, Y=0):
		#     1         1
		# 1 1   1 1 1 1   1 1
		#     1         1
		penta = [
				[0, 1, 0],
				[0, 1, 0],
				[1, 0, 1],
				[0, 1, 0],
				[0, 1, 0],
				[0, 1, 0],
				[0, 1, 0],
				[1, 0, 1],
				[0, 1, 0],
				[0, 1, 0]]
		
		self.drawShape(penta, X, Y)

	def addGG(self, X=0, Y=0):
		# ........................O...........
		# ......................O.O...........
		# ............OO......OO............OO
		# ...........O...O....OO............OO
		# OO........O.....O...OO..............
		# OO........O...O.OO....O.O...........
		# ..........O.....O.......O...........
		# ...........O...O....................
		# ............OO......................

		gg = [
		[0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
		[0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
		[0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
		[0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
		[0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
		[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
		[0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
		[0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
		[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
		[0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
		[0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
		[0, 0, 1, 1, 0, 0, 0, 0, 0, 0],]

		self.drawShape(gg, X, Y)


	def drawShape(self, shape, X=0, Y=0):
		for i, x in enumerate(shape):
			for j, y in enumerate(shape[i]):
				if shape[i][j] == 1:
					self.board[X + i][Y + j] = shape[i][j]


class Game:
	gameloop = 0
	def __init__(self, ip, port, x, y):
		self.x = x
		self.y = y
		self.screen = flashentaschen.Screen(ip, port, x, y)
		self.canvas = flashentaschen.Canvas(x, y)
		self.life = GameOfLife(x, y)
		self.life.addGG(10, 10)

	def setMockDisplay(self, window):
		self.window = window

	def loop(self):
		self.life.drawTo(self.canvas) 
		self.screen.push(self.canvas.print())
		self.canvas.printMock(self.window)
		self.gameloop = Timer(0.1, self.loop)
		self.gameloop.start()

	def stop(self):
		self.gameloop.cancel()


def main():

	game = Game('10.14.10.25', 1337, 50, 50)

	root = Tk()
	root.title("Game of Life")
	frame = Frame(root)
	frame.focus_set()
	gameview = StringVar()
	Label(root, textvariable=gameview, font="Monospace").pack()

	game.setMockDisplay(gameview)	
	game.loop()

	frame.pack()
	root.mainloop()
	game.stop()
		

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
