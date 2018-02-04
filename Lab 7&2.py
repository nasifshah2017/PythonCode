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


