#Syed Nasif Ali Shah

# Lab 7.1A

setMediaPath("H:\CSC 128")

from time import clock

def picCopy(source, canvas, sBeginX, sBeginY, sEndX, sEndY):
 start = clock()
 pixelsCopied = 0 
 rowsCopied = 0 
 targetX = 0 
 for x in range(sBeginX, sEndX):
   targetY = 0 
   for y in range(sBeginY, sEndY):
     pixelsCopied += 1
     color = getColor(getPixel(source,x,y))
     setColor(getPixel(canvas,targetX,targetY), color)
     targetY += 1 
   targetX += 1
   rowsCopied += 1
 print "Time to run function :",clock()-start
 print "There are a total of %d pixels copied" %(pixelsCopied)
 print "There are a total of %d columns copied" %(rowsCopied)
 show(photo)
 show(canvas)
photo = makePicture(getMediaPath("horse.jpg"))
canvas = makeEmptyPicture(163,308)
picCopy(photo, canvas, 104, 114, 267, 422)



setMediaPath("H:\CSC 128")


def copyPortionSource(source, canvas):
 colorSplash = makeColor(216,169,143)
 targetX = 0
 for x in range(50,267):
   targetY = 0
   for y in range(40,380):
     color = getColor(getPixel(source,x,y))
     if distance(color,colorSplash) < 40:
       setColor(getPixel(canvas,targetX,targetY), black)
     else:
       setColor(getPixel(canvas,targetX,targetY), color)
     targetY = targetY + 1
   targetX = targetX + 1
 show(canvas)
 return canvas


