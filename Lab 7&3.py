setMediaPath("H:\CSC 128")

def createCollage2():
 flower1=makePicture(getMediaPath("flower1.jpg"))
  print flower1
 flower2=makePicture(getMediaPath("flower2.jpg"))
  print flower2
 canvas=makePicture(getMediaPath("640x480.jpg"))
  print canvas
 copy(flower1,canvas,0,getHeight(canvas)-getHeight(flower1)-5)
 copy(flower2,canvas,100,getHeight(canvas)-getHeight(flower2)-5)
 #Third picture, flower1 negated
  negative(flower1)
copy(flower1,canvas,200,getHeight(canvas)-getHeight(flower1)-5)
  #Fourth picture, flower2 with no blue
  clearBlue(flower2)
copy(flower2,canvas,300,getHeight(canvas)-getHeight(flower2)-5)
 #Fifth picture, flower1, negated with decreased red
decreaseRed(flower1)
copy(flower1,canvas,400,getHeight(canvas)-getHeight(flower2)-5)
 return canvas

 
 
createCollage2()
 
