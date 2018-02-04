

#Part 3


setMediaPath("H:\CSC 128")

def writeFrame(num,directory,framepict):
    # Have to deal with single digit vs. double digit frame numbers differently
    framenum=str(num)
    if num < 10:
      writePictureTo(framepict,directory+"//frame00"+framenum+".jpg")
    if num >= 10 and num<100:
      writePictureTo(framepict,directory+"//frame0"+framenum+".jpg")
    if num >= 100:
      writePictureTo(framepict,directory+"//frame"+framenum+".jpg")

def slowsunset(directory):
  canvas = makePicture(getMediaPath("beach.jpg"))
  for frame in range(0,100): #99 frames
    printNow("Frame number: "+str(frame))
    makeSunset(canvas)
    # Now, write out the frame
    writeFrame(frame,directory,canvas)

def makeSunset(picture):
  for p in getPixels(picture):
    value=getBlue(p)
    setBlue(p,value*0.99) #Just 1% decrease!
    value=getGreen(p)
    setGreen(p,value*0.99)
    
    
    
    
    
slowsunset("H:\CSC 128")
#playMovie(rectM)
