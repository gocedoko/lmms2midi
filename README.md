# lmms2midi
Basic converter of an LMMS project file into a MIDI file format

1. Introduction
  This is a very basic converter that copies every LMMS track into a corresponding MIDI track.
  It has only basic functionality - it doesn't convert automation tracks or effects, 
  and it doesn't map instruments.

  However, if you set an instrument's MIDI Output channel, it will be also set in the MIDI file.

  Everyone interested in contribution is more than welcome. 
  
2. System requirements:
  - Python 2.6 or higher
  - midiutil python library (https://github.com/duggan/midiutil)

3. Usage
  python lmms2midi.py input.mmp output.mid


Notes
  Please note: This converter works with uncompressed LMMS project files only. 

  So you first need to save the project with the .mmp extension
  (add it manually to the filename in the Save Project dialog).
