import flaschentaschen
import time
screen = flaschentaschen.Screen("10.8.0.159",1337,8,10)
canvas = flaschentaschen.Canvas(8,10)
rainbow_param = 0

while True:
    rainbow_param+=10
    for x in range(0,8):
        for y in range(0,10):
            canvas.point([x,y],canvas.rainbow(rainbow_param+25*(x+y)))
    screen.push(canvas.printScreen(8,10))
    time.sleep(0.1)


