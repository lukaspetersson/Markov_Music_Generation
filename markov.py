import numpy as np


notes = ['C',"^C" ,'D',"^D", 'E', 'F',"^F", 'G',"^G", 'A',"^A", 'B', 'c',"^c", 'd',"^d", 'e', 'f',"^f", 'g',"^g", 'a',"^a", 'b']
chords = ['C', 'G', 'Am', 'F'] 

Nbars = 15

#markov for notes
N = np.array([[0.1, 0.1, 0.2, 0.1, 0.3, 0.0, 0.0, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
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

#NC = np.array([[s,0,s,0,0,s,0,s,0,s,0,0,s,0],
#               [s,0,s,0,s,0,0,s,0,s,0,s,0,0],
#               [0,s,0,s,0,s,0,0,s,0,s,0,s,0],
#               [0,0,s,0,s,0,s,0,0,s,0,s,0,s],
#               [s,0,0,s,0,s,0,s,0,0,s,0,s,0],
#               [0,s,0,0,s,0,s,0,s,0,0,s,0,s]])

#t = 1/3
#NC = np.array([
#               [t,0,t,0,0,t,0,0,0,0,0,0,0,0],
#               [t,0,t,0,t,0,0,0,0,0,0,0,0,0],
#               [0,t,0,t,0,t,0,0,0,0,0,0,0,0],
#               [0,0,t,0,t,0,t,0,0,0,0,0,0,0],
#               [t,0,0,t,0,t,0,0,0,0,0,0,0,0],
#               [0,t,0,0,t,0,t,0,0,0,0,0,0,0],
#
#               [0,t,0,0,t,0,t,0,0,0,0,0,0,0],
#
#               [t,0,t,0,0,t,0,0,0,0,0,0,0,0],
#               [t,0,t,0,t,0,0,0,0,0,0,0,0,0],
#               [0,t,0,t,0,t,0,0,0,0,0,0,0,0],
#               [0,0,t,0,t,0,t,0,0,0,0,0,0,0],
#               [t,0,0,t,0,t,0,0,0,0,0,0,0,0],
#               [0,t,0,0,t,0,t,0,0,0,0,0,0,0],
#
#               [0,t,0,0,t,0,t,0,0,0,0,0,0,0]
#               ])

p = 1/14
C = np.array([
                [p,0,p,0,p,p,0,p,0,p,0,p,p,0,p,0,p,p,0,p,0,p,0,p],
                [p,0,p,0,p,0,p,p,0,p,0,p,p,0,p,0,p,0,p,p,0,p,0,p],
                [p,0,p,0,p,p,0,p,0,p,0,p,p,0,p,0,p,p,0,p,0,p,0,p],
                [p,0,p,0,p,p,0,p,0,p,p,0,p,0,p,0,p,p,0,p,0,p,p,0]
            ]


#NNC = np.multiply(N, NC)
#for row in NNC:
#    row /= sum(row) 
#
#C = np.array([[s, s, s, s, s, s],
#              [s, s, s, s, s, s],
#              [s, s, s, s, s, s],
#              [s, s, s, s, s, s],
#              [s, s, s, s, s, s],
#              [s, s, s, s, s, s]])

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
f.write('Q: "Vivace" 1/4 = 30\n')
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

def next(note, chord):
    #element wise multiply and normalize
    M = np.multiply(N[note],C[chord])
    M /= sum(M)

    r = np.random.rand()
    j = -1
    sum = 0
    while sum < r:
        j = j + 1
        sum = sum + M[j]
    return j

bar = ['*', '2','*', '2','*', '2','*', '2']
tune = ''

k = 0
chord = np.random.randint(0,len(chords))
note = next(np.random.randint(0, len(notes)), chord)

while k < Nbars:
    n = len(bar)
    newbar = '|'+'"'+chords[chord]+'"'
    for j in range(0, n):
        if bar[j] != '*':
            newbar = newbar + bar[j]
        else:
            newbar = newbar + notes[note] 
            note = next(chord, NC)
    
    newbar = newbar + ' '
    tune = tune + newbar
    k += 1

    # the last chord should be C
    if k + 4 > Nbars and chord == "0":
        break
    else:
        #loop chords in same order
        chord = (chord+1)%4


tune = tune + '|\n'

f.write(tune)
f.close()

from music21 import converter
s = converter.parse('out.abc')
s.write('midi', fp = 'out.mid')
