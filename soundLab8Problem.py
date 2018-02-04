#find the normalization ratio of the sound
def normalizeRatio(sound):
  largest = getSampleValueAt(sound, 0)
  for sample in getSamples(sound):
    if largest < getSampleValue(sample):
      largest = getSampleValue(sample)
  #get the normalization ratio
  ratio = 32767.0/largest
  return ratio
  
#normalize first second
def NormalizeFirstSecond(sound):
  rate = int (getSamplingRate(sound))
  seconds = int (getDuration(sound))
  ratio = normalizeRatio(sound)
  #normalize the first second of the sound
  if seconds >= 1:
    #normalize the first second
    for index in range(0,rate): #might have problem if sound is less than 1 second
      value = getSampleValueAt(sound, index)
      setSampleValueAt(sound, index, value *ratio)
    #put all the rest as 0.8 of the normalization  
    #might have problem if sound is less than 1 second
  starting = int (rate)
  ending =  getLength(sound)
  for index in range(starting, ending): 
    value = getSampleValueAt(sound, index)
    setSampleValueAt(sound, index, value *ratio*0.8)
  play(sound)
s=makeSound(getMediaPath("preamble.wav"))
#NormalizeFirstSecond(s)


#normalize first  second and decrease 2 seconds
def NormalizeFirstSecondDecrease2SecondDecreaseRest(sound):
  rate = int (getSamplingRate(sound))
  seconds = int (getDuration(sound))
  ratio = normalizeRatio(sound)
  #normalize the first second of the sound
  if seconds >= 2:
    #normalize the first second
    for index in range(0,rate): #might have problem if sound is less than 1 second
      value = getSampleValueAt(sound, index)
      setSampleValueAt(sound, index, value *ratio)
    #put all the rest as 0.8 of the normalization  
    #might have problem if sound is less than 1 second
    starting = int (rate)
    ending =   int (rate *2)
    for index in range(starting, ending): 
      value = getSampleValueAt(sound, index)
      setSampleValueAt(sound, index, value *ratio*0.8)
    
  starting = int (rate*2)
  ending =  getLength(sound)
  for index in range(starting, ending): 
    value = getSampleValueAt(sound, index)
    setSampleValueAt(sound, index, value *ratio*0.8*0.8)
  play(sound)
s=makeSound(getMediaPath("preamble.wav"))
#NormalizeFirstSecondDecrease2SecondDecreaseRest(s)

#normalize first second and decrease 3 seconds
def NormalizeFirstSecondDecrease3SecondDecreaseRest(sound):
  rate = int (getSamplingRate(sound))
  seconds = int (getDuration(sound))
  ratio = normalizeRatio(sound)
  #normalize the first second of the sound
  if seconds >= 3:
    #normalize the first second
    for index in range(0,rate): #might have problem if sound is less than 1 second
      value = getSampleValueAt(sound, index)
      setSampleValueAt(sound, index, value *ratio)
    #put all the rest as 0.8 of the normalization  
    #might have problem if sound is less than 1 second
    starting = int (rate)
    ending =   int (rate *2)
    for index in range(starting, ending): 
      value = getSampleValueAt(sound, index)
      setSampleValueAt(sound, index, value *ratio*0.8)
    starting = int (rate*2)
    ending =   int (rate *3)
    for index in range(starting, ending): 
      value = getSampleValueAt(sound, index)
      setSampleValueAt(sound, index, value *ratio*0.8*0.8)
      
  starting = int (rate*3)
  ending =  getLength(sound)
  for index in range(starting, ending): 
    value = getSampleValueAt(sound, index)
    setSampleValueAt(sound, index, value *ratio*0.8*0.8*0.8)
  play(sound)
s=makeSound(getMediaPath("preamble.wav"))
#NormalizeFirstSecondDecrease3SecondDecreaseRest(s)

#normalize first second and decrease 3 seconds
def NormalizeFirstSecondDecrease3SecondDecreaseRestTowardsLoopVersion(sound):
  rate = int (getSamplingRate(sound))
  seconds = int (getDuration(sound))
  ratio = normalizeRatio(sound)
  #normalize the first second of the sound
  if seconds >= 3:
    #normalize the first second
    starting = 0 #(0*rate)
    ending = rate #(1*rate)
    for index in range(starting,ending): #might have problem if sound is less than 1 second
      value = getSampleValueAt(sound, index)
      setSampleValueAt(sound, index, value *ratio) #value *ratio*1 =value *ration *0.8**0
    #put all the rest as 0.8 of the normalization  
    #might have problem if sound is less than 1 second
    starting = int (rate) #(1*rate)
    ending =   int (rate *2) #(2*rate)
    for index in range(starting, ending): 
      value = getSampleValueAt(sound, index)
      setSampleValueAt(sound, index, value *ratio*0.8)#value *ratio * 0.8 =value *ration *0.8**1
    starting = int (rate*2)
    ending =   int (rate *3)
    for index in range(starting, ending): 
      value = getSampleValueAt(sound, index)
      setSampleValueAt(sound, index, value *ratio*0.8*0.8) #value *ration *0.8**2
      
  starting = int (rate*3)
  ending =  getLength(sound)
  for index in range(starting, ending): 
    value = getSampleValueAt(sound, index)
    setSampleValueAt(sound, index, value *ratio*0.8*0.8*0.8)#value *ration *0.8**3
  play(sound)
s=makeSound(getMediaPath("preamble.wav"))
#NormalizeFirstSecondDecrease3SecondDecreaseRestTowardsLoopVersion(s)


#lab8.3 normalize and then decrease  
def NormalizeDecrease(sound):
  rate = int (getSamplingRate(sound))
  ratio = normalizeRatio(sound)
  seconds = int (getDuration(sound))
  
  for interval in range(1, seconds):
    starting = int (rate * (interval -1))
    ending = int (rate * interval)
    for index in range(starting,ending):
      value = getSampleValueAt(sound, index)
      setSampleValueAt(sound, index, value * ratio)
    ratio = ratio * 0.8
  starting = rate * seconds
  ending = getLength(sound)
  for index in range(starting,ending):
      value = getSampleValueAt(sound, index)
      setSampleValueAt(sound, index, value *ratio)
  play(sound)
s=makeSound(getMediaPath("preamble.wav"))
NormalizeDecrease(s)


