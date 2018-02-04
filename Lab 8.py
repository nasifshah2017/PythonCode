#Syed Nasif Ali Shah
#Lab - 8.1 & 8.2

#Lab 8.1

setMediaPath("H:\CSC 128")
sound = makeSound(getMediaPath("vote.wav"))

def VolumeNamed(sound):
 for sample in getSamples(sound):
  value = getSampleValue(sample)
  setSampleValue(sample, value*2)
  
VolumeNamed(sound)
play (sound)
explore(sound)


#Lab: 8.2

def VolumeMultiplier(sound, multiplier):
  for sample in getSamples(sound):
   value = getSampleValue(sample)
   setSampleValue(sample, value*multiplier)

VolumeMultiplier(sound,3)
play (sound)
#explore (sound)




  
