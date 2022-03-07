import math
import turtle

########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help

#fred.goto(50,60)
#wn.exitonclick()

##fred.goto(43,96)
##fred.goto(98,-76)
#fred.goto(-85,62)
#fred.goto(105,63)

#for plot in range ():
  #drawSineCurve=(-360,360)







def drawSineCurve(fred=None):
  fred.goto(-360,0)
  for i in range(-360,361):#this is the X value = i
  #second value is always exclusive ex if you goto 1-10 it is really 1-9
    generating_values = math.sin(math.radians(i))#this is where Y values are generated 
    fred.down()
    fred.goto(i,generating_values)
  fred.up()

def setupWindow(wn=None):
  wn.reset()
  wn.setworldcoordinates (-360 , -1 , 360 , 1)

def setupAxis(dart=None):
  dart.up()
  dart.goto(-360,0)
  dart.down()
  dart.goto(360,0)
  dart.up()
  dart.goto(0,1)
  dart.down()  
  dart.goto(0,-1)
  dart.up()


  
def drawCosineCurve(dart):
  dart.goto(-360,1)
  for i in range (-360,361):
   generating_values = math.cos(math.radians(i))
   dart.down()
   dart.goto(i,generating_values)
  dart.up()

def drawTangentCurve(dart):
  dart.goto(-360,0)
  for i in range (-360,361):
    generating_values = math.tan(math.radians(i))
    dart.down()
    dart.goto(i,generating_values )
  dart.up()



##########  Do Not Alter Any Code Past Here ########
def main(): #this is how you create a function
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
