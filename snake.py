#!/usr/bin/python3

import socket
import random
import time

screen_x = range(8)
screen_y = range(5)


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

screen = [[3*[0] for _ in screen_y]  for _ in screen_x]

def point(xy,color=[255,255,255]):
    screen[int(xy[0])][int(xy[1])] = color

def line(a,b,color=[255,255,255]):
    point(a, color)
    point(b, color)
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
            point([x,y], color)
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
            point([x, y], color)
     
def square(a,b,color=[255,255,255]):
    for y in range(b[1] - a[1]):
        for x in range(b[0] - a[0]):
            screen[a[0]+x+1][a[1]+y+1] = color

def rainbow(stage):
    t = stage % 768
    if(stage < 256):
        color = [255-t,t,0]
        
    if(stage > 255 & stage < 512):
        t -= 256
        color = [0,255-t,t]

    if(stage > 511 & stage < 768):
        t -= 256
        color = [t,0,255-t] 

    return color

def randomxy():
    return [random.randint(0,7), random.randint(0,4)]

def color(color):
    for y in screen_y:
        for x in screen_x:  
            screen[x][y] = color

def clear():
    color([0,0,0])

def screen_matrix_to_bytes(data):
    result = bytearray()
    for row in screen_y:
        for col in screen_x:
            for color in range(3):
                result.append(screen[col][row][color])
    return result

def display(ip, port, data):
    mock_display(data)
    header = b"P6\n8 5\n255\n"
    b = screen_matrix_to_bytes(data)
    sock.sendto(header + b, (ip, port))

def mock_display(data):
    for row in screen_y:
        for col in screen_x:
            if(screen[col][row] != [0,0,0]):
                print("#", end='')
            else:
                print("_", end='')
        print()
    

if __name__ == "__main__":

    snake = [[0, 0] for _ in range(8*5)]
    length = 1
    
    food = randomxy()
    snake.insert(0, randomxy())

    while True:
        text = input()

        
        if(text == "w"):
            snake.insert(0, [snake[0][0], (snake[0][1]-1)%5])
        
        if(text == "s"):
            snake.insert(0, [snake[0][0], (snake[0][1]+1)%5])
        
        if(text == "a"):
            snake.insert(0, [(snake[0][0]-1)%8, snake[0][1]])
        
        if(text == "d"):
            snake.insert(0, [(snake[0][0]+1)%8, snake[0][1]])
        
        rainbowstate = 0
        clear()
        for i, pos in enumerate(snake):

            if(food == snake[0]):
                length += 1
                food = randomxy()

            if(i == length):
                break

            point(pos, rainbow(rainbowstate))
            rainbowstate += 32
            rainbowstate %= 768
            
            point(food)

            if(snake[i][0] == snake[0][0] and snake[i][1] == snake[0][1] and i!=0):
                length = 1
                color([255,0,0])
                print("Game Over")
                break

        display("192.168.88.166", 1337, screen)
