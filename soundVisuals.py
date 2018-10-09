import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

#opening wav file to read
spf = wave.open('sample.wav','r')
channel = spf.getnchannels() #1=mono, 2=stereo

#getting frames

frames = spf.getnframes()

#framerate
rate = spf.getframerate()

#length
length=frames/float(rate)

#If mono
if channel == 1:
    print ('Channel: Mono')

signal =spf.readframes(-1)
signal = np.frombuffer(signal, 'Int16')



plt.figure(1)
plt.title('Signal Wave...')
plt.plot(signal)
plt.show()
