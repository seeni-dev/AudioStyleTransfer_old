import soundfile as sf
from scipy import signal
import matplotlib.pyplot as plt
import  pylab

def readFlacFile(path):
    '''

    :param path: path to the sound file
    :return: data (acutal data) sample rate(the rate at which music is sampled
    '''

    try:
        with open(path,"rb") as file:
            data,samplerate=sf.read(file)
        return data,samplerate
    except:
        raise  Exception("Invalid Path")


def plotSpectroGram(data,samplerate):
    '''

    :param data: sample data
    :param samplerate: sample rate
    :return: plots teh frequency
    '''
    plt.specgram(data,Fs=samplerate)
    plt.show()
    return

def getSpectroGram(path):
    '''

    :param data: sample data
    :param samplerate: sample rate
    :return: returns the image of the spectrogram
    '''
    data,samplerate=readFlacFile(path)
    plt.specgram(data,Fs=samplerate)
    plt.show() #todo 1 Find a way to return the spectrogram as an image
    return

def test():
    path="/mnt/Backup/Dataset/Extract/LibriSpeech/dev-clean/84/121123/84-121123-0000.flac"
    data,samplerate=readFlacFile(path)
    plotSpectroGram(data,samplerate)
    return

if __name__ == '__main__':
    test()
