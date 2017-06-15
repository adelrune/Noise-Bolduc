from pyo import *
from os.path import isfile
from os import listdir
import re
from random import choice

s = Server(audio="jack").boot()
s.setMidiInputDevice(1)

notes = {'c':0,'c#':1,'d':2,'d#':3,'e':4,'f':5,'f#':6,'g':7,'g#':8,'a':9,'a#':10, 'b':11}
def note_name_to_midi(filename):
    note = filename.split('_')[2]
    note_name = re.match("[a-g][#b]?", note).group()
    pitch = notes[note_name] + int(note[-1]) * 12
    return pitch

sounds = [[] for i in range(200)]

for note_file in listdir("norm"):
    if isfile("norm/" + note_file):
        print(note_file, note_name_to_midi(note_file))
        sounds[note_name_to_midi(note_file)].append("norm/" + note_file)

players = [0 for i in range(16)]
n_player = 0

def start_new_note(event, note, velocity):
    global n_player
    if(event != 144 or velocity == 0):
        return
    player = SfPlayer(choice(sounds[note]))
    n_player = (n_player + 1) % 16
    players[n_player] = player
    player.out()
    player.start()

midi_in = RawMidi(start_new_note)

s.start()
s.gui(locals)
