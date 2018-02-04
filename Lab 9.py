# Syed Nasif Ali Shah (201304650)
# Lab 9.1

setMediaPath("H:\CSC 128")
sound1 = makeSound(getMediaPath("vote.wav"))
sound2 = makeSound(getMediaPath("mark.wav"))



def addSoundInto(sound1, sound2):
  for sampleNmr in range(0, getLength(sound1)):
      sample1 = getSampleValueAt(sound1, sampleNmr)
      sample2 = getSampleValueAt(sound2, sampleNmr)
      setSampleValueAt(sound2, sampleNmr, sample1 + sample2)
      
      
      
def MakeNewSound():
  source1 = sound1
  source2 = sound2
  length1 = getLength(source1)
  length2 = getLength(source2)
  source3 = makeEmptySound(length1 + length2)
  targetIndex = 0
  for target in range(0, (length1)/2):
    sample = getSampleValueAt(source1, target)
    setSampleValueAt(source3, targetIndex, sample)
    targetIndex = targetIndex + 1
    
  for target in range(0, min(length1, length2)):
    sample1 = getSampleValueAt(source1, target)
    sample2 = getSampleValueAt(source2, target)
    setSampleValueAt(source3, targetIndex, sample1+sample2)
    targetIndex = targetIndex + 1
    
  for target in ((length2)/2, length2-1):
    sample = getSampleValueAt(source2, target)
    setSampleValueAt(source3, targetIndex, sample)
    targetIndex = targetIndex + 1
  
  play(source3)
  explore(source3)
  return source3
  
#Lab 9.2

def lab92v1():
  source1 = myNormalize(makeSound("vote.wav"))
  source2 = myNormalize(makeSound("mark.wav"))
  length1 = getLength(source1)
  length2 = getLength(source2)
  pieces = 5
  w1 = 0.75
  w2 = (1- w1)*1.0
  len = min(length1, length2)
  target = makeEmptySound(pieces * len)
 
  for piece in range(0, pieces):
    for index in range (0, len):
      sample1 = getSampleValueAt(source1, index)
      sample2 = getSampleValueAt(source2, index)
      setSampleValueAt(target, index + len * piece, sample1 * w1 + sample2 * w2)
    w1 = w1 -0.1
    w2 = 1 - w1
  play(target)
  explore(target)
  return target
      




