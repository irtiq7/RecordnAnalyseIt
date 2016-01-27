'''I wrote this program to record an audio from
the source and replay the file as soon as the audio
is recorded. I also wanted to see the waveform of the
audio so that I could introduce noise cancellation
technique in the later part of the project. I am adding
the source code here so that if you are doing something
similar then do let me know. Feel free to use this code
to get yourself started.
'''

import pyaudio
import wave
from Tkinter import *
from matplotlib import pyplot as plt
import numpy as np



CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
#~ RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = 'C:\Users\USA\Desktop\output.wav'

def recording():
	RECORD_SECONDS = recordtime()
	p = pyaudio.PyAudio()
	frames = []
	stream = p.open(format=FORMAT,
					channels=CHANNELS,
					rate=RATE,
					input=True,
					frames_per_buffer=CHUNK)
	print("* Recording")
	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		data = stream.read(CHUNK)
		frames.append(data)
	
	print("* Done recording")

	stream.stop_stream()
	stream.close()
	p.terminate()

	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()

def playrecording():

	print '* Play Recording'
	if len(WAVE_OUTPUT_FILENAME) < 2:
		print "Plays a wave file.\n\n" +\
			  "Usage: %s.wav" % WAVE_OUTPUT_FILENAME[0]
		sys.exit(-1)

	wf = wave.open(WAVE_OUTPUT_FILENAME, 'r')

	p = pyaudio.PyAudio()

	# open stream
	stream = p.open(format =
					p.get_format_from_width(wf.getsampwidth()),
					channels = wf.getnchannels(),
					rate = wf.getframerate(),
					output = True)

	# read data
	data = wf.readframes(CHUNK)

	# play stream
	while data != '':
		stream.write(data)
		data = wf.readframes(CHUNK)

	stream.close()
	p.terminate()

def plotdata():
	print '* Plot Data'
	spf = wave.open(WAVE_OUTPUT_FILENAME,'r')

	#Extract Raw Audio from Wav File
	signal = spf.readframes(-1)
	signal = np.fromstring(signal, 'Int16')
	fs = spf.getframerate()

	#If Stereo
	#~ if spf.getnchannels() == 2:
		#~ print 'Just mono files'

	Time=np.linspace(0, len(signal)/fs, num=len(signal))

	plt.figure(1)
	plt.title('Signal Wave...')
	plt.plot(Time,signal)
	plt.show()

def recordtime():
	e = E1.get()
	#~ print e
	return int(e)
	
def main():
	recording()
	#~ stoprecording()
	playrecording()
	plotdata()

root = Tk()
top = Frame(root).pack()
bottom = Frame(root).pack()
Label(top, text= 'REPLAY RECORDED AUDIO').pack()
Label(top, text= 'AND').pack()
Label(top, text= 'PLOT THE RESULTS').pack()
Label(top, text= '').pack()
Label(top, text= '').pack()
Label(top, text="Enter time duration to record").pack()
E1 = Entry(top, text='Enter time')
E1.focus_set()
E1.pack()
Button(bottom, text='RECORD', command= main).pack(side=BOTTOM)

root.mainloop()


import pyaudio
import wave
from Tkinter import *
from matplotlib import pyplot as plt
import numpy as np



CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
#~ RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = 'C:\Users\USA\Desktop\output.wav'

def recording():
	RECORD_SECONDS = recordtime()
	p = pyaudio.PyAudio()
	frames = []
	stream = p.open(format=FORMAT,
					channels=CHANNELS,
					rate=RATE,
					input=True,
					frames_per_buffer=CHUNK)
	print("* Recording")
	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		data = stream.read(CHUNK)
		frames.append(data)
	
	print("* Done recording")

	stream.stop_stream()
	stream.close()
	p.terminate()

	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()

def playrecording():

	print '* Play Recording'
	if len(WAVE_OUTPUT_FILENAME) < 2:
		print "Plays a wave file.\n\n" +\
			  "Usage: %s.wav" % WAVE_OUTPUT_FILENAME[0]
		sys.exit(-1)

	wf = wave.open(WAVE_OUTPUT_FILENAME, 'r')

	p = pyaudio.PyAudio()

	# open stream
	stream = p.open(format =
					p.get_format_from_width(wf.getsampwidth()),
					channels = wf.getnchannels(),
					rate = wf.getframerate(),
					output = True)

	# read data
	data = wf.readframes(CHUNK)

	# play stream
	while data != '':
		stream.write(data)
		data = wf.readframes(CHUNK)

	stream.close()
	p.terminate()

def plotdata():
	print '* Plot Data'
	spf = wave.open(WAVE_OUTPUT_FILENAME,'r')

	#Extract Raw Audio from Wav File
	signal = spf.readframes(-1)
	signal = np.fromstring(signal, 'Int16')
	fs = spf.getframerate()

	#If Stereo
	#~ if spf.getnchannels() == 2:
		#~ print 'Just mono files'

	Time=np.linspace(0, len(signal)/fs, num=len(signal))

	plt.figure(1)
	plt.title('Signal Wave...')
	plt.plot(Time,signal)
	plt.show()

def recordtime():
	e = E1.get()
	#~ print e
	return int(e)
	
def main():
	recording()
	#~ stoprecording()
	playrecording()
	plotdata()

root = Tk()
top = Frame(root).pack()
bottom = Frame(root).pack()
Label(top, text= 'REPLAY RECORDED AUDIO').pack()
Label(top, text= 'AND').pack()
Label(top, text= 'PLOT THE RESULTS').pack()
Label(top, text= '').pack()
Label(top, text= '').pack()
Label(top, text="Enter time duration to record").pack()
E1 = Entry(top, text='Enter time')
E1.focus_set()
E1.pack()
Button(bottom, text='RECORD', command= main).pack(side=BOTTOM)

root.mainloop()
