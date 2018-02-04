# Syed Nasif Ali (ID - 201304650)
setMediaPath("H:\CSC 128") 

def copyPictureSideways():
  
  file = getMediaPath("barbara.jpg")
  picture = makePicture(file)
  canvasfile = getMediaPath("640x480.jpg")
  canvas = makePicture(canvasfile)

  targetX = 0
  for sourceX in range(0,getWidth(picture)):
    targetY = 0
    for sourceY in range(0,getHeight(picture)):
      colour = getColor(getPixel(picture,sourceX,sourceY))
      setColor(getPixel(canvas,targetY,targetX), colour)
      targetY += 1
    targetX += 1
  show(picture)
  show(canvas)
  return canvas
copyPictureSideways()