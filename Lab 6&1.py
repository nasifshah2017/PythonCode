#file = pickAFile()
#print "print file: ", file

setMediaPath("H:\CSC 128")
picture = makePicture(getMediaPath("barbara.jpg")

def mirrorBotTop(picture):
 midPicture = getHeight(picture)/2
 height = getHeight(picture)
 for x in range (0,getWidth(picture)):
  for y in range(0,midPicture):
   topPixel = getPixel(picture,x,y)
   bottomPixel = getPixel(picture,x,height - y -1)
   color = getRed(bottomPixel)
   setRed(topPixel,color)

mirrorBotTop(picture)
  




#decrease red
#def decreaseRed(picture):
# for p in getPixels(picture):
  #value=getRed(p)
 # setRed(p,value*0.7)
  
#decreaseRed(picture)