#Syed Nasif Ali Shah (201304650)
#Lab: 8.3


setMediaPath("H:\CSC 128")
sound = makeSound(getMediaPath("vote.wav"))

def increaseAndDecrease(sound):
 largest = getSampleValueAt(sound, 0)
 for s in getSamples(sound):
  if largest < getSampleValue(s):
   largest = getSampleValue(s)
 ratio = 32767.0/largest
 return ratio

#find the normalization ratio of the sound
def normalizeRatio(sound):
  largest = getSampleValueAt(sound, 0)
  for sample in getSamples(sound):
    if largest < getSampleValue(sample):
      largest = getSampleValue(sample)
  #get the normalization ratio
  ratio = 32767.0/largest
  return ratio
  
  
def normalizeDecrease2Second(sound):
 rate = int (getSamplingRate(sound)) #Number of samples in 1 second
 seconds = int (getDuration(sound)) #Number of seconds in the sound
 ratio = normalizeRatio(sound)
 if seconds >= 2:
  #First second
  starting = 0
  ending = rate
  for index in range(0, rate):
   value = getSampleValueAt(sound, index)
   setSampleValueAt(sound, index, value*ratio)
  #Second second
  starting = rate
  ending = rate*2
  for index in range(starting, ending):
   value = getSampleValueAt(sound, index)
   setSampleValueAt(sound, index, value*ratio*0.8)
  #The Rest
  starting = rate*2
  ending = getLength(sound)
  for index in range (starting, ending):
   value = getSampleValueAt(sound, index)
   setSampleValueAt(sound, index, value*ratio*0.8)

increaseAndDecrease(sound)
normalizeDecrease2Second(sound)
play (sound)

#find the normalization ratio of the sound
def normalizeRatio(sound):
  largest = getSampleValueAt(sound, 0)
  for sample in getSamples(sound):
    if largest < getSampleValue(sample):
      largest = getSampleValue(sample)
  #get the normalization ratio
  ratio = 32767.0/largest
  return ratio
  
