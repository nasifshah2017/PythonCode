def makeLeftSquare():
  w = makeWorld()
  t = makeTurtle(w)
  for x in range(0,4):
    forward(t,50)
    turnLeft(t)
    
#makeLeftSquare()

def moveTurtleTo():
  w = makeWorld()
  t = makeTurtle(w)
  moveTo(t, 150, 150)
  
#moveTurtleTo()

def DrawThreeSquare():
  w = makeWorld()
  t = makeTurtle(w)
  for num in range(0,3):
    for x in range(0,4):
      forward(t,50)
      turnLeft(t)
    penUp(t)
    forward(t,60)
    penDown(t)
    
#DrawThreeSquare()


def DrawThreeTriangle():
  w = makeWorld()
  t = makeTurtle(w)
  for num in range(0,3):
    for x in range(0,3):
      forward(t,20+10*num)
      turn(t, 120)
    penUp(t)
    forward(t,60)
    penDown(t)
    
#DrawThreeTriangle()

def DrawPolygon(n):
  w = makeWorld()
  t = makeTurtle(w)
  for x in range(0,n):
    forward(t,50)
    turn(t, 360/n)
    
#DrawPolygon(3)

def DrawSomePolygons(m):
  w = makeWorld()
  t = makeTurtle(w)
  for num in range(3,m):
     DrawPolygon(num)
    
#DrawSomePolygons(6)


def DrawPolygonsTogether(m):
  w = makeWorld()
  t = makeTurtle(w)
  for num in range(3,m):
    for n in range(0,num):
      forward(t,50)
      turn(t, 360/num)
    
DrawPolygonsTogether(6)