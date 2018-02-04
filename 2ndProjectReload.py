
#Part 2

setMediaPath("H:\CSC 128")

def makeRectMovie(directory ):
 for num in range (1, 30): #29 Frames
  canvas = makeEmptyPicture (300, 200)
  topaz = makeEmptyPicture (300, 200)
  addRectFilled(canvas, num*5, num*7, 50, 50, green) #Object 1
  addRectFilled(canvas, 200-(num*5), num*7, 50, 50, blue)  #Object 2
  #convert the number to a string
  numStr = str(num)
  if num < 10:
   writePictureTo(canvas, directory+"\\frame0"+numStr+".jpg")
  if num >= 10:
   writePictureTo(canvas, directory+"\\frame"+numStr+".jpg")
   
 movie = makeMovieFromInitialFile(directory+"\\frame00.jpg")
 return movie

rectM = makeRectMovie("H:\CSC 128")
playMovie(rectM)