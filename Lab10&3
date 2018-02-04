# Syed Nasif Ali Shah
# Lab 10.2

setMediaPath("H:\CSC 128")

def squareWave(freq,amplitude): 
 
  square = makeSound(getMediaPath("sec3silence.wav"))
  
  samplingRate = getSamplingRate(square)
  seconds = 3
 
  interval = 1.0 * seconds / freq
  
  samplesPerCycle = interval * samplingRate
 
  samplesPerHalfCycle = int(samplesPerCycle / 2)
  sampleVal = amplitude
  s  = 1
  i = 1
  print samplesPerHalfCycle
  for s in range (0, getLength(square)):
   
    if (i > samplesPerHalfCycle):
      print "index = , ", s, " i = ", i
      
      sampleVal *= (-1)
      
      i = 0
    setSampleValueAt(square,s,sampleVal)
    i += 1
  return(square)
  

def triangleWave(freq,amplitude): 
  
  triangle = makeSound(getMediaPath("sec3silence.wav"))
 
  samplingRate = getSamplingRate(triangle)
  seconds = 3 
  interval = 1.0 * seconds / freq
  
  samplesPerCycle = interval * samplingRate
 
  samplesPerHalfCycle = int(samplesPerCycle / 2)
  sampleVal = amplitude
  s  = 1
  i = 1
  print samplesPerHalfCycle
  for s in range (0, getLength(square)):
    
    if (i > samplesPerHalfCycle):
      print "index = , ", s, " i = ", i
     
      sampleVal *= (-1)
     
      i = 0
    setSampleValueAt(triangle,s,sampleVal)
    i += 1
  return(triangle)

def addWaves(sound1, sound2):
   for sampleNmr in range(0, min(getLength(sound1),getLength(sound2))):
      sample1 = getSampleValueAt(sound1, sampleNmr)
      sample2 = getSampleValueAt(sound2, sampleNmr)
      setSampleValueAt(sound2, sampleNmr, sample1 + sample2)

square = squareWave(5,7)
triangle_v = triangleWave(5,7)
addWaves(square, triangle_v)
 