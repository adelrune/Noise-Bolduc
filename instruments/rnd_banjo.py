from pyo import *
from os.path import isfile
from os import listdir
import re
from random import choice

s = Server(audio="jack").boot()
s.setMidiInputDevice(1)

# notes = {'c':0,'c#':1,'d':2,'d#':3,'e':4,'f':5,'f#':6,'g':7,'g#':9,'a':10,'a#':11}
# def note_name_to_midi(filename):
#     note = filename.split("/")[1].split('_')[1]
#     note_name = re.match("[a-g][#b]?", note).group()
#     pitch = notes[note_name] * note[-1] * 12

sounds = [[] for i in range(200)]

for note_file in listdir("snds"):
    if isfile("snds/" + note_file):
        sounds[i].append("snds/" + note_file)

players = []

def start_new_note(event, note, velocity):
    if(event != 144):
        return
    player = SfPlayer(sounds[note])
    players.append(player)
    player.out()

midi_in = RawMidi(scale=0)

s.start()
s.gui(locals)