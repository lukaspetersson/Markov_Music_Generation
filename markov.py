import numpy as np

def next(now, M):
    r = np.random.rand()
    j = -1
    sum = 0
    while sum < r:
        j = j + 1
        sum = sum + M[now, j]
    return j

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'c', 'd', 'e', 'f', 'g', 'a', 'b']
Nnotes = len(notes)
startnote = 3

Nbars = 5

#markov for notes
M = np.array([[0.1, 0.1, 0.2, 0.1, 0.3, 0.0, 0.0, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
              [0.0, 0.1, 0.1, 0.1, 0.3, 0.3, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
              [0.1, 0.0, 0.1, 0.1, 0.0, 0.3, 0.3, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0],
              [0.0, 0.1, 0.1, 0.2, 0.0, 0.1, 0.4, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0],
              [0.2, 0.2, 0.0, 0.0, 0.1, 0.1, 0.1, 0.2, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0],
              [0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.0, 0.2, 0.0, 0.0, 0.1, 0.0],
              [0.0, 0.0, 0.1, 0.2, 0.1, 0.1, 0.2, 0.0, 0.1, 0.1, 0.0, 0.0, 0.0, 0.1],
              [0.1, 0.0, 0.0, 0.0, 0.1, 0.1, 0.0, 0.1, 0.1, 0.2, 0.1, 0.2, 0.0, 0.0],
              [0.0, 0.1, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.0],
              [0.0, 0.0, 0.1, 0.0, 0.0, 0.1, 0.0, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.0],
              [0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3],
              [0.0, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.1, 0.2, 0.2, 0.0, 0.2, 0.1, 0.1],
              [0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.2, 0.2, 0.1, 0.1, 0.2, 0.1],
              [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.0, 0.0, 0.1, 0.4, 0.1, 0.1, 0.1]])

#template for possible bars
#bars = [['(', '*', '3', ' ', '*', ')', '*', '*'],
#        ['*', '4', ' ', '*', '2'],
#       ['*', '3', ' ', '*', '*', '2'],
#        ['*', '2', ' ', '(', '*', '*', '*', '*', ')']]

#markov for bars
#N = np.array([[0.5, 0.2, 0.2, 0.1],
#              [0.5, 0, 0.2, 0.3],
#              [0.5, 0.2, 0, 0.3],
#              [0.6, 0.1, 0.1, 0.2]])

f = open("out.abc", "w")

f.write('%%abc-charset utf-8\n')
f.write('%%titlefont NewCenturySchlbk-Roman 22\n')
f.write('%%subtitlefont NewCenturySchlbk 16\n')
f.write('%%composerfont NewCenturySchlbk-Italic 14\n')
f.write('%%footerfont NewCenturySchlbk 16\n')
f.write('%%headerfont NewCenturySchlbk 16\n')
f.write('%%tempofont NewCenturySchlbk-Bold 15\n')
f.write('X:1\n')
f.write('T:Markovtest\n')
f.write('C:strauss (localhost)\n')
f.write('L:1/8\n')
f.write('M:4/4\n')
f.write('R:walz\n')
# 180=presto, 160=vivace, 132=allegro, 96=moderato, 72=andante
f.write('Q: "Vivace" 1/4 = 40\n')
f.write('V:1\n')
f.write('K:C\n')
f.write('%%MIDI channel 1\n')
#f.write('%%MIDI program 1 48\n') # strängar
#f.write('%%MIDI program 1 0\n') # piano
f.write('%%MIDI program 1 22\n')
f.write('%%MIDI chordprog 0\n')
f.write('%%MIDI chordvol 40\n')
f.write('%%MIDI drum ddd 60 61 61 50 40 40\n')
f.write('%%MIDI drumon\n')

bar = ['*', '2','*', '2','*', '2','*', '2']
tune = ''

k = 0
note = next(np.random.randint(0, len(notes)), M)

while k < Nbars:
    n = len(bar)
    newbar = '| '
    for j in range(0, n):
        if bar[j] != '*':
            newbar = newbar + bar[j]
        else:
            newbar = newbar + notes[note]
            note = next(note, M)

    newbar = newbar + ' '
    tune = tune + newbar
    k += 1

tune = tune + '|\n'

f.write(tune)
f.close()

from music21 import converter
s = converter.parse('out.abc')
s.write('midi', fp = 'out.mid')
