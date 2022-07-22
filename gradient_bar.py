from graphics import *

def main():
    win = GraphWin("Gradient Bar")
    win.setBackground("white")
    win.setCoords(400, 400, 400, 400)
    
   
    gradientbar = Rectangle(Point(0,0), Point (1, 0))
    gradientbar.setFill("green")
    gradientbar.setwidth(10)
    gradientbar.draw(win)
    
    for i in range(6):
        gradientbar = Rectangle(Point(i, 0), Point(i + 1, 0))
        gradientbar.setFill("green")
        gradientbar.setWidth(10)
        gradientbar.draw(win)
        
    
    win.close()

main()
