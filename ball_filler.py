import math

ball= int(input("How many bowling balls will be manufactured? "))
diam = float(input("What is the diameter of each ball in inches? "))
core = int(input(" What is the core volume in inches cubed? "))
    
radius = diam/2
totalvol = ((4/3) * math.pi*(radius)*(radius)*(radius))
filvol = (totalvol - core) * ball
    
print( "You will need", filvol, "inches cubed of filler")
    
    