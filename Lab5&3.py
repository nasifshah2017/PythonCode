#Syed Nasif Ali Shah

#Lab 5.3

setMediaPath("H:\CSC 128")

picture = makePicture(getMediaPath("beach.jpg"))

def reduceBlue(picture):
 for p in getPixels (picture):
  value = getBlue(p)
  setBlue(p, value*.7)
def reduceGreen(picture):
 for p in getPixels(picture):
  value = getGreen(p)
  setGreen(p, value*.7)
  
def makeSunset(picture):
 reduceBlue(picture)
 reduceGreen(picture)
 
makeSunset(picture) 