#Nathan Raia

from graphics import *

def drawTrafficLight(x , y):
    drawBody(x , y , 900 , 700)
    drawLamp("red" , 500 , 250 , 100)
    drawLamp("yellow" , 500 , 500 , 100)
    drawLamp("green" , 500 , 750 , 100)
    
def drawBody(x , y , width , length):
    body = Rectangle(Point(x , y) , Point(length , width))
    body.setFill("white")
    body.draw(win)
    
def drawLamp(color , x , y , radius):
    lamp = Circle(Point(x , y) , radius)
    lamp.setFill(color)
    lamp.draw(win)
    
win = GraphWin("Traffic Light" , 1000 , 1000)
drawTrafficLight(300 , 100)