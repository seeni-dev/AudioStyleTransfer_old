import Spectrogram.Spectrogram as Spec
import os

def testAllFiles():
    dirPath="/mnt/Backup/Dataset/Extract/LibriSpeech/dev-clean/84/121123"
    files=os.listdir(dirPath)
    for file in files:
        exten=file[-4:]
        filePath=os.path.join(dirPath,file)
        print(filePath)
        if(exten=="flac"):
            data,samplerate=Spec.readFlacFile(filePath)
            Spec.plotSpectroGram(data,samplerate)

if __name__ == '__main__':
    testAllFiles()
