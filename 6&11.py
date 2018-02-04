#Syed Nasif Ali (ID - 201304650)

setMediaPath("H:\CSC 128")
picture = makePicture(getMediaPath("barbara.jpg"))

def mirrorBotTop(picture):
 midPicture = getHeight(picture)/4
 height = getHeight(picture)
 for x in range (0, getWidth(picture)):
  for y in range(height, midPicture):
   px = getPixel(picture,x,y)
   color = getRed(px)
   setRed(px, color)
 show(picture)
 return picture

mirrorBotTop(picture)

