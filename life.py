#!/usr/bin/env python3
"""
Flaschentaschen Game of Life
"""

__author__ = "Marcin Jasiukowicz"
__version__ = "0.1.0"
__license__ = "MIT"

import flaschentaschen
import time
import random
from copy import deepcopy
from tkinter import Tk, Frame, Label, StringVar
from threading import Timer

class GameOfLife:
	def __init__(self, X, Y):
		self.width = X
		self.height = Y
		self.board = [[0 for y in range(Y)] for x in range(X)]

	def loop(self):
		next_frame = deepcopy(self.board)
	
		for x in range(len(self.board)):
			for y in range(len(self.board[x])):
				neighbours = self.checkNeighbours(x, y)
				if self.board[x][y] == 1:
					if neighbours > 3:
						next_frame[x][y] = 0
					if(neighbours == 2):
						next_frame[x][y] = 1
					if(neighbours == 3):
						next_frame[x][y] = 1
					if neighbours < 2:
						next_frame[x][y] = 0	
				if self.board[x][y] == 0:
					if(neighbours == 3):
						next_frame[x][y] = 1

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
		for x in range(len(self.board)):
			for y in range(len(self.board[x])):
				if self.board[x][y] == 1:
					canvas.point([x,y])

	def addRandom(self, points):
		for _ in range(points):
			self.board[random.randint(0,self.width-1)][random.randint(0,self.height-1)] = 1

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

	def addPentomino(self, X=0, Y=0):
		#   1 1
		# 1 1
		#   1
		pentomino = [
				[1, 0, 0],
				[1, 1, 1],
				[0, 1, 0]]
		
		self.drawShape(pentomino, X, Y)

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

		for x in range(len(shape)):
			for y in range(len(shape[x])):
				if shape[x][y] == 1:
					self.board[X + x % self.width][Y + y % self.height] = shape[x][y]


class Game:
	gameloop = 0
	def __init__(self, ip, port, x, y):
		self.x = x
		self.y = y
		self.screen = flaschentaschen.Screen(ip, port, x, y)
		self.canvas = flaschentaschen.Canvas(x, y)
		self.life = GameOfLife(x, y)
		#self.life.addRandom(int((x*y)/2))
		self.life.addPentomino(int(x/2), int(y/2))

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

    game = Game('10.8.0.159', 1337, 100, 50)

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
