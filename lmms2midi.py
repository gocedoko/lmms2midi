#!/usr/bin/python

from xml.dom import minidom
from midiutil.MidiFile import MIDIFile
import sys


if len(sys.argv) > 2:

	inFile = minidom.parse(sys.argv[1])
	outFile = open(sys.argv[2], 'wb')

	midiData = MIDIFile(len(inFile.getElementsByTagName('track')))

	tempo = int(inFile.getElementsByTagName('head')[0].attributes['bpm'].value)
	trackCnt=0

	for t in inFile.getElementsByTagName('track'):
		if t.getElementsByTagName('midiport'):
			channel = int(t.getElementsByTagName('midiport')[0].attributes['outputchannel'].value)

			midiData.addTrackName(trackCnt, channel, str(t.attributes['name'].value))
			midiData.addTempo(trackCnt, channel, tempo)

			for p in t.getElementsByTagName('pattern'):
				startPos = float(p.attributes['pos'].value)

				for note in p.getElementsByTagName('note'):
					midiData.addNote(	
						track		  =	  trackCnt, 				  \
						channel 	= 	channel, 						\
						pitch 		=	  int(note.attributes['key'].value)+24, 			            \
						time		  =	  (startPos + float(note.attributes['pos'].value))/48.0, 	\
						duration	=	  float(note.attributes['len'].value)/48.0,		            \
						volume		=	  int(note.attributes['vol'].value))

			trackCnt += 1

	midiData.writeFile(outFile)
	outFile.close()

else:
	print("\nUsage:\t\tpython " + sys.argv[0] + " input.mmp output.mid\n")
