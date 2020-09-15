#!/usr/bin/env python3
"""
Flaschentaschen common abstractions
"""


__author__ = "Marcin Jasiukowicz"
__version__ = "0.1.0"
__license__ = "MIT"


import socket


class Screen:
	def __init__(self, ip, port, x, y):
		self.screen = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		#sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
		self.ip = ip
		self.port = port
		self.screen_x = x
		self.screen_y = y
		
	def screen_matrix_to_bytes(self, data):
		result = bytearray()
		for y in range(self.screen_y):
			for x in range(self.screen_x):
				for color in range(3):
					result.append(data[x][y][color])
		return result
	
	def push(self, data):
		header = b"P6\n%d %d\n255\n" % (self.screen_x, self.screen_y)
		b = self.screen_matrix_to_bytes(data)
		self.screen.sendto(header + b, (self.ip, self.port))


class Canvas:
	def __init__(self, x,y):
		self.canvas_x = x
		self.canvas_y = y
		self.body = [[3*[0] for _ in range(y)]  for _ in range(x)]


	def point(self, xy,color=[255,255,255]):
		self.body[int(xy[0])][int(xy[1])] = color

	def line(self, a,b,color=[255,255,255]):
		self.point(a, color)
		self.point(b, color)
		x = a[0]
		y = a[1]
		if (a[0] < b[0]):
			xi = 1
			dx = b[0] - a[0]
		else:
			xi = -1
			dx = a[0] - b[0]

		if (a[1] < b[1]):
			yi = 1
			dy = b[1] - a[1]
		else:
			yi = -1
			dy = a[1] - b[1]
		
		if (dx > dy):
			ai = (dy - dx) * 2
			bi = dy * 2
			d = bi - dx
			while (x != b[0]):
				if (d >= 0):
					x += xi
					y += yi
					d += ai
				else:
					d += bi
					x += xi
				self.point([x,y], color)
		else:     
			ai = ( dx - dy ) * 2
			bi = dx * 2
			d = bi - dy
			while (y != b[1]):

				if (d >= 0):
					x += xi
					y += yi
					d += ai
				else:
					d += bi
					y += yi
				self.point([x, y], color)
		
	def square(self, a,b,color=[255,255,255]):
		for y in range(b[1] - a[1]):
			for x in range(b[0] - a[0]):
				self.body[a[0]+x+1][a[1]+y+1] = color

	def rainbow(self, stage):
		t = stage % 768
		if(t < 256):
			return ([255-t,t,0])
			
		elif(t < 512):
			t -= 256
			return ([0,255-t,t])

		else:
			t -= 512
			return ([t,0,255-t])

	def color(self, color):
		for y in range(self.canvas_y):
			for x in range(self.canvas_x):  
				self.body[x][y] = color

	def clear(self):
		self.color([0,0,0])

	def printMock(self, frame):
		string = ''
		for y in range(self.canvas_y):
			for x in range(self.canvas_x):
				if(self.body[x][y] != [0,0,0]):
					string += '#'
				else:
					string += ' '
			string += '\n'
		frame.set(string)


	def printScreen(self, size_x, size_y, offset_x=0, offset_y=0):
		returnBody = [[3*[0] for _ in range(size_y)]  for _ in range(size_x)]
		for y in range(size_y):
			for x in range(size_x):  
				returnBody[x][y] = self.body[offset_x + x][offset_y + y]
				
		return returnBody

	def print(self):
		return self.body
