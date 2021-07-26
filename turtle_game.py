
#Author: Mahsoud
#INFT1004 Assignment1
#Task1: Draw a maze and get the route
#Task2: Draw your name and student number using the turtle
from time import sleep
def assignment():
  height = requestInteger("Please enter a height greater than 800")
  width = requestInteger("Please enter a width greater than 800")
  if height > 800:
    if width > 800:
      
        
  
  #creating a multiplier so that it can work with different heights and widths
  
      earth = makeWorld(height,width)
      ben = smartTurtle(earth)
      ben.penWidth = 4
      ben.setColor(black)
      ben.penUp()
      ben.backward(109)
      ben.penDown()
      ben.forward(44)
      ben.turn(270)
      ben.circle1()
      ben.turn(280)
      ben.forward(157)
      ben.penUp()
      ben.backward(109)
      ben.turnRight()
      ben.penDown()
      ben.circle2()
      ben.turnLeft()
      ben.forward(100)
      ben.penUp()
      ben.backward(40)
      ben.turnRight()
      ben.penDown()
      ben.circle3()
      ben.circle3()
      ben.circle3()
      ben.turnLeft()
      ben.forward(43)
      ben.penUp()
      ben.backward(43)
      ben.turnRight()
      ben.circle3()
      ben.circle3()
      ben.penDown()
      ben.circle3()
      ben.penUp()
      ben.turnLeft()
      ben.forward(40)
      ben.turnRight()
      ben.circle4()
      ben.penDown()
      ben.circle4()
      ben.turnRight()
      ben.forward(40)
      ben.penUp()
      ben.backward(40)
      ben.turnLeft()
      ben.penDown()
      ben.circle4()
      ben.turnLeft()
      ben.forward(56)
      ben.penUp()
      ben.backward(56)
      ben.turnRight()
      ben.circle4()
      ben.forward(12)
      ben.penDown()
      ben.circle4()
      ben.penUp()
      ben.circle4()
      ben.penDown()
      ben.circle4()
      ben.circle4()
      ben.penUp()
      ben.circle4()
      ben.penDown()
      ben.circle4()
      ben.circle4()
      ben.turnLeft()
      ben.forward(50)
      ben.penUp()
      ben.backward(50)
      ben.turnRight()
      ben.circle4()
      ben.forward(10)
      ben.penDown()
      ben.turn(96)
      ben.forward(100)
      ben.penUp()
      ben.backward(100)
      ben.turn(-96)
      ben.penDown()
      ben.circle4()
      ben.circle4()
      ben.turnLeft()
      ben.forward(50)
      ben.penUp()
      ben.backward(50)
      ben.turnRight()
      ben.forward(5)
      ben.circle4()
      ben.turn(7)
      ben.forward(20)
      ben.penDown()
      ben.circle4()
      ben.forward(7)
      ben.penUp()
      ben.turn(-85)
      ben.forward(50)
      ben.turnRight()
      ben.penDown()
      ben.forward(7)
      ben.circle5()
      ben.circle5()
      ben.circle5()
      ben.circle5()
      ben.circle5()
      ben.circle5()
      ben.circle5()
      ben.circle5()
      ben.penUp() 
      ben.circle5()
      ben.backward(10)
      ben.penDown()
      ben.turn(86)
      ben.forward(55)
      ben.penUp()
      ben.backward(55)
      ben.turn(-86)
      ben.penDown()
      ben.forward(7)
      ben.circle5()
      ben.forward(7)
      ben.circle5()
      ben.circle5()
      ben.circle5()
      ben.circle5()
      ben.circle5()
      ben.circle5()
      ben.circle5()
      ben.penUp()
      ben.circle5()
  
      sleep(3)
      ben.turn(84)
      ben.forward(494)
      ben.turn(180)
      sleep(5)
      countDown()
      ben.penWidth = 10
      ben.setColor(green)
      ben.penDown()
      ben.turnRight()
      ben.fill1()
      ben.turn(-80)
      ben.forward(90)
      ben.turn(45)
      ben.forward(130)
      ben.turn(45)
      ben.forward(90)
      ben.turnLeft()
      ben.forward(80)
      ben.turnRight()
      ben.forward(20)
      ben.penUp()
      ben.forward()
      ben.penWidth = 4
    else:
      showError("Please rerun the program and follow the instructions")
      return
      
  else:
    showError("Please rerun the program and follow the instructions")
    return
    
    
  
  
  
  
  

class smartTurtle(Turtle):
  
  def circle1(self):
    for i in range(17):
      self.turn(10)
      self.forward(10)
  
  def circle2(self):
    for i in range(15):
      self.turn(6)
      self.forward(10)
  
  def circle3(self):
    for i in range(9):
      self.turn(5)
      self.forward(14)
 
  def circle4(self):
    for i in range(11):
      self.turn(2)
      self.forward(7)
  
  def circle5(self):  
    for i in range(5):
      self.forward(18)
      self.turn(4)
  
  def fill1(self):  
    for i in range(16):
      self.turn(-6)
      self.forward(24)

def countDown():
  count = makeSound(getMediaPath("Countdown.wav"))
  blockingPlay(count)