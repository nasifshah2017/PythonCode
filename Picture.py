def sunset(picture):
  for px in getPixels(picture):
    red = getRed(px)
    green = getGreen(px)
    setGreen(px, green * 0.3)
    blue = getBlue(px)
    setBlue(px, blue * 0.3)
file = pickAFile()
picture = makePicture(file)
show(picture)
sunset(picture)
repaint(picture)




