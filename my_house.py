from graphics import *

def main():
        win=GraphWin("Home",500,500)
        win.setCoords(0,0,200,200)
        win.setBackground("white")

    
        cir = Circle(Point(30,180),20)
        cir.draw(win)
        cir.setFill("yellow")
        
        rec = Rectangle(Point(90,0),Point(170,120))
        rec.draw(win)
        rec.setFill("brown")
    
        rec2 = Rectangle(Point(160,95),Point(130,60))
        rec2.draw(win)
        rec2.setFill("blue")
        
        rec3 = Rectangle(Point(160,50),Point(100,20))
        rec3.draw(win)
        rec3.setFill("blue")
        
        lin = Line(Point(180, 95),Point(90, 50))
        lin.draw(win)
        lin.setOutline("light blue")
        lin.setFill("light blue")
        
        lin = Line(Point(95,180),Point(90,50))
        lin.draw(win)
        lin.setOutline("light blue")
        lin.setFill("light blue")
             
       
main()

