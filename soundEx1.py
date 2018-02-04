"""
filename=pickAFile()
print filename
sound = makeSound(filename)
print sound
#samples = getSamples(sound)
#print samples
print getSampleValueAt(sound, 1)
print getSampleValueAt(sound, 2)
explore(sound)

print getLength(sound)
"""

#setMediaPath()

#Recipe to Increase the Volume

def increaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample,value * 2)
    
    
#filename=pickAFile()
#s=makeSound(filename)
sOrigin=makeSound(getMediaPath("airplane.wav"))
print "original sound value at sample 1 and 2"
print getSampleValueAt(sOrigin,1)
print getSampleValueAt(sOrigin,2)

s=makeSound(getMediaPath("airplane.wav"))
increaseVolume(s)
writeSoundTo(s, getMediaPath("test1.wav"))
print "original sound value at sample 1 and 2"
print getSampleValueAt(sOrigin,1)
print getSampleValueAt(sOrigin,2)
print "increase volume by 2:  sound value at sample 1 and 2"
print getSampleValueAt(s,1)
print getSampleValueAt(s,2)


#More generic
def changeVolume(sound , factor):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample ,value * factor)
    
s2=makeSound(getMediaPath("airplane.wav"))
changeVolume(s2,0.5)
print "original sound value at sample 1 and 2"
print getSampleValueAt(sOrigin,1)
print getSampleValueAt(sOrigin,2)
print "after change volume by a factor 0.5, sound value at sample 1 and 2"
print getSampleValueAt(s2,1)
print getSampleValueAt(s2,2)


#Maxing (normalizing) the sound
def myNormalize(sound):
  largest = 0
  for s in getSamples(sound):
    largest = max(largest, getSampleValue(s))
  amplification = 32767.0 / largest
  print "Largest sample value in the original sound was", largest
  print "Amplication multiplier is ", amplification
  
  for s in getSamples(sound):
    louder = amplification * getSampleValue(s)
    setSampleValue(s, louder)
    
myNormalize(s2)    
print getSampleValueAt(s2,1)
print getSampleValueAt(s2,2)

#another method: Maxing (normalizing) the sound
def myNormalize2(sound):
  largest = 0
  for s in getSamples(sound):
    if  getSampleValue(s) > largest:
      largest = getSampleValue(s)
  amplification = 32767.0 / largest
  print "Largest sample value in the original sound was", largest
  print "Amplication multiplier is ", amplification
  
  for s in getSamples(sound):
    louder = amplification * getSampleValue(s)
    setSampleValue(s, louder)
    
 
 
s2=makeSound(getMediaPath("airplane.wav")) 
myNormalize2(s2)    
print getSampleValueAt(s2,1)
print getSampleValueAt(s2,2)


#All clipping, all the time
def onlyMaximize(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if value > 0:
      setSampleValue(sample, 32767)
    if value < 0:
      setSampleValue(sample, -32767)
onlyMaximize(s2)
#play(s2)

def splicePreamble():
  file = getMediaPath("preamble10.wav")
  source = makeSound(file)
  target = makeSound(file) # This will be the newly spliced sound
  targetIndex = 17408
  for sourceIndex in range (33414, 40052): #where the word "United" is in the sound
    setSampleValueAt(target, targetIndex, getSampleValueAt(source, sourceIndex))
    targetIndex = targetIndex + 1
  for sourceIndex in range(17408, 26726): # where the word "People" is in the sound
    setSampleValueAt(target, targetIndex, getSampleValueAt(source, sourceIndex))
    targetIndex = targetIndex + 1
  for index in range(0, 1000):
    setSampleValueAt(target, targetIndex,0)  #stick some quiet space
    targetIndex = targetIndex + 1
  play(target)
  return target

#splicePreamble()

def clip(source, start, end):
  target = makeEmptySound(end - start)
  tIndex = 0
  for sIndex in range(start, end):
    value = getSampleValueAt(source, sIndex)
    setSampleValueAt(target, tIndex, value)
    tIndex = tIndex + 1
  return target

def copy(source, target, start):
  tIndex = start
  for sIndex in range(0, getLength(source)):
    value = getSampleValueAt(source, sIndex)
    setSampleValueAt(target, tIndex, value)
    tIndex = tIndex + 1

def createNewPreamble():
  file = getMediaPath("preamble10.wav")
  preamble = makeSound(file)         # old preamble
  united = clip(preamble, 33414, 40052) # "United"
  start = clip(preamble, 0, 17407)      # "We the"
  end = clip(preamble, 17408, 55510)    # the rest
  len = getLength(start) + getLength(united)
  len = len + getLength(end)  # length of everything
  newPre = makeEmptySound(len)       # new preamble
  copy(start, newPre, 0)
  copy(united, newPre, getLength(start))
  copy(end, newPre, getLength(start)+getLength(united))
  play(newPre)
  return newPre
  
#createNewPreamble()

def reverse(source):
  target = makeEmptySound(getLength(source))
  sourceIndex = getLength(source) - 1 # start at end
  for targetIndex in range(0, getLength(target)):
    value = getSampleValueAt(source, sourceIndex)
    setSampleValueAt(target, targetIndex, value)
    sourceIndex = sourceIndex - 1 # move backwards
  play(target)
  return target
  
file = getMediaPath("preamble10.wav")
preamble = makeSound(file)         # old preamble
#reverse(preamble)
 
 
def mirrorSound(sound):
  len = getLength(sound)
  mirrorpoint = len/2
  for index in range(0, mirrorpoint):
    left = getSampleObjectAt(sound, index)
    right = getSampleObjectAt(sound, len-index-1)
    value = getSampleValue(left)
    setSampleValue(right, value)
  play(sound)

#mirrorSound(preamble)
