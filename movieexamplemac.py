def makeRectMovie(directory ):
  for num in range (1 ,30): #29 frames (1 to 29)
    canvas = makeEmptyPicture (300 ,200)
    addRectFilled(canvas ,num * 10, num * 5, 50,50, red)
    # convert the number to a string
    numStr=str(num)
    if num < 10:
      writePictureTo(canvas ,directory+"/frame0"+numStr+".jpg")
    if num >= 10:
      writePictureTo(canvas ,directory+"/frame"+numStr+".jpg")
  movie = makeMovieFromInitialFile(directory+"/frame00.jpg");
 
  return movie

#rectMovie = makeRectMovie("/Users/manlin/Documents/2016-spring/W/cs128/examples/testmovie")
#playMovie(rectMovie)


def tickertape(directory,string):
  for num in range(1,50): #99 frames
    canvas = makeEmptyPicture(300,100)
    #Start at right, and move left
    addText(canvas,300-(num*10),50,string)
    # Now, write out the frame
    # Have to deal with single digit vs. double digit frame numbers differently
    numStr=str(num)
    if num < 10:
      writePictureTo(canvas,directory+"/frame0"+numStr+".jpg")
    if num >= 10:
      writePictureTo(canvas,directory+"/frame"+numStr+".jpg")
  movie = makeMovieFromInitialFile(directory+"/frame00.jpg");
  return movie
  
#stringMovie = tickertape("/Users/manlin/Documents/2016-spring/W/cs128/examples/testmovie", "Hello, How are you, Thank you")
#playMovie(stringMovie)



def copy(source, target, targX, targY):
  targetX = targX
  for sourceX in range(0,getWidth(source)):
    targetY = targY
    for sourceY in range(0,getHeight(source)):
      px=getPixel(source,sourceX,sourceY)
      tx=getPixel(target,targetX,targetY)
      setColor(tx,getColor(px))
      targetY=targetY + 1
    targetX=targetX + 1


#Clip() function returns part of another picture.Using general copy() function we defined earlier.
def clip(picture ,startX ,startY ,endX ,endY ):
	width = endX - startX + 1
	height = endY - startY + 1
	resPict = makeEmptyPicture(width ,height)
	resX = 0
	for x in range(startX ,endX ):
	  resY =0 # reset result y index
	  for y in range(startY ,endY ):
	     origPixel = getPixel(picture ,x,y)
	     resPixel = getPixel(resPict ,resX ,resY)
	     setColor(resPixel ,( getColor(origPixel )))
	     resY=resY + 1
	  resX=resX + 1
	return resPict
 

def moveHead(directory ):
  markF=getMediaPath("blue-mark.jpg")
  mark = makePicture(markF)
  head = clip(mark ,275 ,160 ,385 ,306)
  for num in range (1 ,30): #29 frames
    printNow("Frame number: "+str(num))
    canvas = makeEmptyPicture (640 ,480)
    # Now , do the actual copying
    copy(head ,canvas ,num*10,num *5)
    # Now , write out the frame
    # Have to deal with frame # digits
    numStr=str(num)
    if num < 10:
      writePictureTo(canvas ,directory+"/frame0"+numStr+".jpg")
    if num >= 10:
      writePictureTo(canvas ,directory+"/frame"+numStr+".jpg")
  movie = makeMovieFromInitialFile(directory+"/frame00.jpg");
 
  return movie

#headMovie = moveHead("/Users/manlin/Documents/2016-spring/W/cs128/examples/testmovie")
#playMovie(headMovie)


def makeSunset(picture):
  for p in getPixels(picture):
    value=getBlue(p)
    setBlue(p,value*0.99) #Just 1% decrease!
    value=getGreen(p)
    setGreen(p,value*0.99)
    
def slowsunset(directory):
  canvas = makePicture(getMediaPath("beach.jpg")) #outside the loop!
  for frame in range(0,30): #99 frames
    printNow("Frame number: "+str(frame))
    makeSunset(canvas)
    # Now, write out the frame
    numStr=str(frame)
    if frame < 10:
      writePictureTo(canvas ,directory+"/frame0"+numStr+".jpg")
    if frame >= 10:
      writePictureTo(canvas ,directory+"/frame"+numStr+".jpg")
  return makeMovieFromInitialFile(directory+"/frame00.jpg")


#sunSetMovie =  slowsunset("/Users/manlin/Documents/2016-spring/W/cs128/examples/testmovie")
#playMovie(sunSetMovie)


def writeFrame(num,directory,framepict):
    # Have to deal with single digit vs. double digit frame numbers differently
    framenum=str(num)
    if num < 10:
      writePictureTo(framepict,directory+"/frame00"+framenum+".jpg")
    if num >= 10 and num<100:
      writePictureTo(framepict,directory+"/frame0"+framenum+".jpg")
    if num >= 100:
      writePictureTo(framepict,directory+"/frame"+framenum+".jpg")
      
      
def moveHead2(directory ):
  markF=getMediaPath("blue-mark.jpg")
  mark = makePicture(markF)
  face = clip(mark ,275 ,160 ,385 ,306)
  for num in range (1 ,30): #29 frames
    printNow("Frame number: "+str(num))
    canvas = makeEmptyPicture (640 ,480)
    # Now , do the actual copying
    copy(face ,canvas ,num*10,num *5)
    # Now , write out the frame
    writeFrame(num ,directory ,canvas)

  movie = makeMovieFromInitialFile(directory+"/frame00.jpg");
  return movie

#headMovie = moveHead2("/Users/manlin/Documents/2016-spring/W/cs128/examples/testmovie")
#playMovie(headMovie)


#fading by background
def swapbg(person, bg, newbg,threshold):  
  for x in range(1,getWidth(person)):
    for y in range(1,getHeight(person)):
      personPixel = getPixel(person,x,y)
      bgpx = getPixel(bg,x,y)
      personColor= getColor(personPixel)
      bgColor = getColor(bgpx)
      if distance(personColor,bgColor) < threshold:
        bgcolor = getColor(getPixel(newbg,x,y))
        setColor(personPixel, bgcolor)


def slowfadeout(directory):
  bg = makePicture(getMediaPath("wall.jpg"))
  jungle = makePicture(getMediaPath("jungle2.jpg"))
  for frame in range(0,100): #99 frames
    canvas = makePicture(getMediaPath("wall-two-people.jpg"))
    printNow("Frame number: "+str(frame))
    swapbg(canvas,bg,jungle,frame)
    # Now, write out the frame
    writeFrame(frame,directory,canvas)
  movie = makeMovieFromInitialFile(directory+"/frame00.jpg");
  return movie

import os
def lightenFish(directory):
  framenum = 0
  for framefile in os.listdir(getMediaPath("fish")):
    framenum = framenum + 1
    printNow("Frame: "+str(framenum))
    if framefile.endswith(".jpg"):
      frame=makePicture(getMediaPath("fish")+"/"+framefile)
      for p in getPixels(frame):
        color = getColor(p)
        if distance(color,black)>8:
          color=makeLighter(color)
          color=makeLighter(color)
          setColor(p,color)
      writeFrame(framenum,directory,frame)
  movie = makeMovieFromInitialFile(directory+"/frame00.jpg");
  return movie

playMovie(lightenFish("/Users/manlin/Documents/2016-spring/W/cs128/examples/testmovie"))
