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
  return sound
  
#setMediaPath()
def MakeNewSound():
  source1 = makeSound("bassoon-c4.wav")
  source2 = makeSound("bassoon-e4.wav")
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
  
#MakeNewSound()



def makeMusic():
  source1 = makeSound("bassoon-c4.wav")
  source2 = makeSound("bassoon-e4.wav")
  source3 = makeSound("bassoon-g4.wav")
  length1 = getLength(source1)
  length2 = getLength(source2)
  length3 = getLength(source3)
  target = makeEmptySound(length1 + length2 + length3)
  targetIndex = 0
  for index in range(0, length1):
    sample = getSampleValueAt(source1, index)
    setSampleValueAt(target, targetIndex, sample)
    targetIndex = targetIndex + 1
  for index in range(0, length2):
    sample = getSampleValueAt(source2, index)
    setSampleValueAt(target, targetIndex, sample)
    targetIndex = targetIndex + 1
  for index in range(0, length3):
    sample = getSampleValueAt(source3, index)
    setSampleValueAt(target, targetIndex, sample)
    targetIndex = targetIndex + 1
  play(target)
  writeSoundTo(target,"music1.wav")
  return target
  
#makeMusic()


def linkMusic(sourcefile1, sourcefile2, targetfile):
  source1 = makeSound(sourcefile1)
  source2 = makeSound(sourcefile2)

  length1 = getLength(source1)
  length2 = getLength(source2)
 
  target = makeEmptySound(length1 + length2)
  targetIndex = 0
  for index in range(0, length1):
    sample = getSampleValueAt(source1, index)
    setSampleValueAt(target, targetIndex, sample)
    targetIndex = targetIndex + 1
  for index in range(0, length2):
    sample = getSampleValueAt(source2, index)
    setSampleValueAt(target, targetIndex, sample)
    targetIndex = targetIndex + 1
  writeSoundTo(target,targetfile)
  return target
  
#linkMusic("music1.wav", "music1.wav", "music.wav")

#repeat each sound 5 times, each time merging with different weight
#only merge upto the min length of each sound
def lab92v1():
  source1 = myNormalize(makeSound("music.wav"))
  source2 = myNormalize(makeSound("preamble.wav"))
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


  
#lab92v1()

#merging the sound into 5 pieces, each piece is merged with different weight
#each piece is 1/5 of the minimal length of the two sound
def lab92v2():
  source1 = myNormalize(makeSound("music.wav"))
  source2 = myNormalize(makeSound("preamble.wav"))
  length1 = getLength(source1)
  length2 = getLength(source2)
  pieces = 5
  w1 = 0.75
  w2 = (1- w1)*1.0
  len = min(length1, length2)
  target = makeEmptySound(len)

  for piece in range(0, pieces):
    for index in range (0, len/pieces):
      sample1 = getSampleValueAt(source1, index + len/pieces * piece)
      sample2 = getSampleValueAt(source2, index + len/pieces * piece)
      setSampleValueAt(target, index + len/pieces * piece, sample1 * w1 + sample2 * w2)
    w1 = w1 -0.1
    w2 = 1 - w1
  play(target)
  explore(target)
  return target

#lab92v2()


#merging the sound into  pieces, each piece is merged with different weight
#each piece is 1/pieces of the minimal length of the two sound
def lab92v3():
  source1 = myNormalize(makeSound("music.wav"))
  source2 = myNormalize(makeSound("preamble.wav"))
  length1 = getLength(source1)
  length2 = getLength(source2)
  pieces = 100
  w1 = 0.75
  w2 = (1- w1)*1.0
  len = min(length1, length2)
  target = makeEmptySound(len)

  for piece in range(0, pieces):
    for index in range (0, len/pieces):
      sample1 = getSampleValueAt(source1, index + len/pieces * piece)
      sample2 = getSampleValueAt(source2, index + len/pieces * piece)
      setSampleValueAt(target, index + len/pieces * piece, sample1 * w1 + sample2 * w2)
    w1 = w1 -0.5/pieces
    w2 = 1 - w1
  play(target)
  explore(target)
  return target

#lab92v3()


 

def lab92v4():
  s2 = myNormalize(makeSound("music.wav"))
  s1 = myNormalize(makeSound("preamble.wav"))
  l1 = getLength(s1)
  l2 = getLength(s2)
  rate = getSamplingRate(s1)
  if(l1 > l2):
    maxlen = l1
  else: 
    maxlen = l2 
  target=makeEmptySound(maxlen)
 
  vol1 = 0.25
  grad1 = 0.5/(l1)
  vol2 = 0.75
  grad2 = 0.5/(l2)
  for index in range(0,maxlen):
    if index<l1:
      sample1=getSampleValueAt(s1,index)
    else:
      vol1=0
    if index<l2:
      sample2=getSampleValueAt(s2,index)
    else:
      vol2=0
    mergedSample = vol1 * sample1 + vol2 * sample2
    setSampleValueAt(target, index, mergedSample)  
    vol1 = vol1 + grad1   
    vol2 = vol2 - grad2
  play(target)
  explore(target)
  return target       

lab92v4() 
 

