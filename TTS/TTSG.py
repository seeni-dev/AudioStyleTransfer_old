from gtts import gTTS
import random
import math
import os
def createSound(text="Welcome . Pass a String to produce any output",lang="en"):
    tts=gTTS(text=text,lang=lang)
    return tts

def playAudio(audtts):
    file="../DATA/"+str(math.floor(random.random()))+str(math.floor(random.random()))+".mp3"
    audtts.save(file)
    #playsound(file)
    os.system("play "+file)
    return


def test():
    tts=createSound("Welcome to Audio Style Transfer")
    playAudio(tts)
    return

def drive():
    text=input("Enter")
    tts = createSound("Welcome to Audio Style Transfer")
    playAudio(tts)
    return


if __name__ == '__main__':
    test()
