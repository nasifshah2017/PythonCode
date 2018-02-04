#Part 3
setMediaPath("H:\CSC 128")

picture = getMediaPath("beach.jpg")

 def clip(picture, 0, 0, 100, 100)
   width = 100 - 0 + 1
   height = 100 - 0 + 1
   resPict = makeEmptyPicture(width, height)
   resX = 0
   for x in range (0, 100)
    resY = 0 #rest result y index
    for y in range (0, 100)
     origPixel = getPixel(picture, x, y)
     resPixel = getPixel(resPict, resX, resY)
     setColor(resPixel, (getColor(origPixel)))
     resY = resY + 1
   resX = resX + 1
return resPict
def moveSun(directory):
 markF = getMediaPath("beach.jpg")
 mark = makePicture(markF)
 sun = clip(mark, 250, 170, 450, 330)
 for num in range (1, 11): # 10 frames
  printNow("Frame number: " + str(num))
  canvas = makeEmptyPicture (640, 480)
  #Now, write out the frame digits
  #Have to deal with frame
  numStr = str(num)
  if num < 10:
   writePictureTo(canvas, directory+"// frameo" +numStr+".jpg")
  if num >= 10:
   writePictureTo(canvas, directory+"// frame" +numStr+".jpg")
   
 movie = makeMovieFromInitialFile(directory+"\\frame00.jpg")
 return movie

rectM = moveSun("H:\CSC 128")
playMovie(rectM)
   
     
       
