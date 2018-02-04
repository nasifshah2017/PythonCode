setMediaPath("H:/CSC 128")
def copyAladdin():

 #Set up and target pictures
 barbf=getMediaPath("barbara.jpg")
 barb = makePicture(barbf)
 canvasf = getMediaPath("640x480.jpg")
 canvas = makePicture(canvasf)
 #Now, do the actual copying
 
 sourceX = 50
 for targetX in range(100,100+((200-0)/2)):
  sourceY = 50
  for targetY in range(100,100+((200-0)/2)):
   color = getColor(getPixel(barb,sourceX,sourceY))
   setColor(getPixel(canvas,targetX,targetY),color)
   sourceY = sourceY + 2
  sourceX = sourceX + 2
  show(barb)
  show(canvas)
  return canvas
copyAladdin()