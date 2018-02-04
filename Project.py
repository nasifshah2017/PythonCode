# Syed Nasif Ali (201304650)
#Project 
#Part 1

setMediaPath("H:\CSC 128")

def makeOvalMovie(directory ):
 for num in range (1, 30): #29 frames 
  canvas = makeEmptyPicture(300, 200)
  # add a filled circle moving linearly
  addOvalFilled(canvas, num/30,num*15,50,50,red) #Object 1
  # Let's have one just moving around
  blueX = 120+ int (10 * sin(num))
  blueY = 6*num+int (10* cos(num))
  addOvalFilled(canvas, blueX, blueY, 50, 50, blue)#Object 2
  #Now, write out the frame
  #have to deal with single digit vs. double digit
  
  numStr = str(num)
  if num < 10:
    writePictureTo(canvas, directory +"\\frame0"+ numStr +".jpg")
  if num >= 10:
    writePictureTo(canvas, directory+"\\frame"+ numStr +".jpg") 
 movie = makeMovieFromInitialFile(directory + "\\frame00.jpg")
 return movie
     
playMovie(makeOvalMovie("H:\CSC 128"))