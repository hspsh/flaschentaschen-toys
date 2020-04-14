#!/usr/bin/env python3
"""
Flaschentaschen snake
"""


__author__ = "Marcin Jasiukowicz"
__version__ = "0.1.0"
__license__ = "MIT"

ip = '10.14.10.25'
ip1 = '10.14.10.67'

import flaschentaschen
import socket
import random
import time
from tkinter import *
from threading import Timer

class Snake:
	length = 1
	map_width = 1
	map_height = 1
	direction = 'd'

	def __init__(self, map_width, map_height):
		self.body = [[0, 0] for _ in range(map_width * map_height)]
		self.map_width = map_width
		self.map_height = map_height
		self.body.insert(0, self.randomxy())
		self.food = self.randomxy()

	def randomxy(self):
		return [random.randint(0,self.map_width-1), random.randint(0,self.map_height-1)]

	def control(self, event):
		key = event.char
		if(key == 'w' or key == 's' or key == 'a' or key == 'd'):
			self.direction = key

	def drawTo(self, canvas):
		if(self.direction == 'w'):
			self.body.insert(0, [self.body[0][0], (self.body[0][1]-1)%self.map_height])
		
		if(self.direction == 's'):
			self.body.insert(0, [self.body[0][0], (self.body[0][1]+1)%self.map_height])

		if(self.direction == 'd'):
			self.body.insert(0, [(self.body[0][0]-1)%self.map_width, self.body[0][1]])

		if(self.direction == 'a'):
			self.body.insert(0, [(self.body[0][0]+1)%self.map_width, self.body[0][1]])

		rainbowstate = 0
		canvas.clear()
		for i, pos in enumerate(self.body):

			if(self.food == self.body[0]):
				self.length += 1
				self.food = self.randomxy()

			if(i == self.length):
				break

			canvas.point(pos, canvas.rainbow(rainbowstate))
			rainbowstate += 32
			rainbowstate %= 768
			
			canvas.point(self.food)

			if(self.body[i][0] == self.body[0][0] and self.body[i][1] == self.body[0][1] and i!=0):
				self.length = 1
				canvas.color([255,0,0])
				break
		return canvas

class Game:
	gameloop = 0
	def __init__(self, ip, ip1, port, x, y):
		self.x = x
		self.y = y
		self.screen = flaschentaschen.Screen(ip, port, int(x/2), y)
		self.screen1 = flaschentaschen.Screen(ip1, port, int(x/2), y)
		self.canvas = flaschentaschen.Canvas(x, y)
		self.snake = Snake(x, y)
		

	def controller(self, event):
		self.snake.control(event)

	def setMockDisplay(self, window):
		self.window = window

	def loop(self):
		self.snake.drawTo(self.canvas) 

		self.screen.push(self.canvas.printScreen(int(self.x/2), self.y))
		self.screen1.push(self.canvas.printScreen(int(self.x/2), self.y, int(self.x/2)))
		self.canvas.printMock(self.window)
		self.gameloop = Timer(0.5, self.loop)
		self.gameloop.start()

	def stop(self):
		self.gameloop.cancel()



def main():
	game = Game(ip, ip1, 1337, 10, 8)
	
	root = Tk()
	root.title("Snake")
	frame = Frame(root)
	frame.focus_set()
	gameview = StringVar()
	Label(root, textvariable=gameview, font="Monospace").pack()

	game.setMockDisplay(gameview)	
	game.loop()

	frame.bind("<Key>", game.controller)
	frame.pack()
	root.mainloop()
	game.stop()

if __name__ == "__main__":
	main()
