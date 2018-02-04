#Syed Nasif Ali

#Lab 10.1 

setMediaPath("H:\CSC 128")

def cosWave(freq, amplitude):
 mySound = getMediaPath('sec1silence.wav') #Get a blank sound
 buildCos = makeSound(mySound)
 sr = getSamplingRate(buildCos) #Sampling rate
 interval = 1.0/freq #Make sure its floating point
 samplesPerCycle = interval * sr #Samples Per Cycle
 maxCycle = 2*pi
 for pos in range (0, getLength(buildCos)):
  rawSample = cos((pos/samplesPerCycle)*maxCycle)
  sampleVal = int(amplitude*rawSample)
  setSampleValueAt(buildCos,pos,sampleVal)
 return buildCos
 
cosWave(2, 3)  