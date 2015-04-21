import serial
import pyaudio
import wave
import sys

class AudioFile:
    chunk = 1024

    def __init__(self, file):
        """ Init audio stream """ 
        self.wf = wave.open(file, 'rb')
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format = self.p.get_format_from_width(self.wf.getsampwidth()),
            channels = self.wf.getnchannels(),
            rate = self.wf.getframerate(),
            output = True
        )

    def play(self):
        """ Play entire file """
        data = self.wf.readframes(self.chunk)
        while data != '':
            self.stream.write(data)
            data = self.wf.readframes(self.chunk)

    def close(self):
        """ Graceful shutdown """ 
        self.stream.close()
        self.p.terminate()

# Usage example for pyaudio
inp=""
ser = serial.Serial('/dev/tty.usbmodem1421', 9600)
while True:
	if ser.inWaiting():
		a = AudioFile("Green_Light_2.wav")
		a.play()
		a.close()
		ser.flushInput()
		inp=""
	else:
		a = AudioFile("Red_Light_2_short.wav")
		a.play()
		a.close()