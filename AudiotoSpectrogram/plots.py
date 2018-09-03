
import numpy
import matplotlib.pyplot as plt
import pylab
from scipy.io import wavfile
from scipy.fftpack import fft

def spectrogram(wavepath):
	myAudio = wavepath
	#Read file and get sampling freq [ usually 44100 Hz ]  and sound object
	samplingFreq, mySound = wavfile.read(wavepath)
	mySoundDataType = mySound.dtype
	#We can convert our sound array to floating point values ranging from -1 to 1 as follows
	mySound = mySound / (2.**15)
	#Check sample points and sound channel for duel channel(5060, 2) or  (5060, ) for mono channel
	mySoundShape = mySound.shape
	samplePoints = float(mySound.shape[0])
	#Get duration of sound file
	signalDuration =  mySound.shape[0] / samplingFreq
	#If two channels, then select only one channel
	mySoundOneChannel = mySound[:,0]
	#Plotting the tone
	timeArray = numpy.arange(0, samplePoints, 1)
	timeArray = timeArray / samplingFreq
	#Scale to milliSeconds
	timeArray = timeArray * 1000
	#Plot the tone
	plt.plot(timeArray, mySoundOneChannel, color='G')
	plt.xlabel('Time (ms)')
	plt.ylabel('Amplitude')
	#plt.show()
	return plt

a = spectrogram("etman.wav")
a.plot()
plt.show()
