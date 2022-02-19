import numpy as np


notes = ['C',"^C" ,'D',"^D", 'E', 'F',"^F", 'G',"^G", 'A',"^A", 'B', 'c',"^c", 'd',"^d", 'e', 'f',"^f", 'g',"^g", 'a',"^a", 'b']
chords = ['C', 'G', 'Am', 'F'] 

Nbars = 40
#markov for notes
<<<<<<< HEAD
=======

>>>>>>> 6f2ccecf2332fc6a19392f515a674a49bd5900f4
N = np.ones([24,24])
f = open("matrix.txt")
for i, line in enumerate(f):
    for j, num in enumerate(line[1:-2].split(', ')):
        N[i][j] = float(num)
<<<<<<< HEAD
=======

>>>>>>> 6f2ccecf2332fc6a19392f515a674a49bd5900f4

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
            ])

D = np.zeros([24,24])
for i in range(24):
    for j in range(24):
        if i == j:
            D[i][j] = 1/10
        else:
            D[i][j] = 1/(abs(i-j)+1.4)
    s = np.sum(D[i])
    D[i] /= s

# bars = np.array([
#     ['*', '1','*', '1','*', '1','*', '1','*', '1','*', '1','*', '1', '*', '1'],
#     ['*', '2','*', '2','*', '2','*', '2'],
#     ['*', '8'],
#     ['*', '4','*', '4'],
#     ['*', '4','*', '2','*', '2'],
#     ['*', '2','*', '4','*', '2'],
#     ['*', '2','*', '2','*', '4'],
#     ['*', '4','*', '2','*', '1','*', '1','*'],
#     ['*', '2','*', '4','*', '1','*', '1','*'],
#     ['*', '1','*', '2','*', '4','*', '1','*'],
#     ['*', '1','*', '4','*', '2','*', '1','*'],
#     ['*', '4','*', '1','*', '1','*', '1','*', '1'],
#     ['*', '1','*', '4','*', '1','*', '1','*', '1'],
#     ['*', '1','*', '1','*', '4','*', '1','*', '1'],
#     ['*', '1','*', '1','*', '1','*', '4','*', '1'],
#     ['*', '1','*', '1','*', '1','*', '1','*', '4'],
#     ['*', '2','*', '2','*', '1','*', '1','*', '1', '*', '1'],
#     ['*', '2','*', '1','*', '1','*', '2','*', '1', '*', '1'],
#     ['*', '1','*', '2','*', '1','*', '1','*', '2', '*', '1'],
#     ['*', '2','*', '1','*', '1','*', '1','*', '1', '*', '2'],
#     ['*', '1','*', '1','*', '2','*', '1','*', '1', '*', '2'],
#     ['*', '1','*', '2','*', '2','*', '1','*', '1', '*', '1']
#     ], dtype=object)

# phrasebars = np.array([
#     ['*', '1','*', '1','*', '1','*', '1','*', '1','*', '1','*', '1', '*', '1'],
#     ['*', '2','*', '2','*', '2','*', '2'],
#     ['*', '4','*', '2','*', '2'],
#     ['*', '2','*', '4','*', '2'],
#     ['*', '2','*', '2','*', '4'],
#     ['*', '4','*', '2','*', '1','*', '1','*'],
#     ['*', '1','*', '2','*', '4','*', '1','*'],
#     ['*', '1','*', '4','*', '2','*', '1','*'],
#     ['*', '4','*', '1','*', '1','*', '1','*', '1'],
#     ['*', '1','*', '1','*', '1','*', '1','*', '4'],
#     ['*', '2','*', '2','*', '1','*', '1','*', '1', '*', '1'],
#     ['*', '2','*', '1','*', '1','*', '2','*', '1', '*', '1'],
#     ['*', '1','*', '2','*', '1','*', '1','*', '2', '*', '1'],
#     ['*', '2','*', '1','*', '1','*', '1','*', '1', '*', '2'],
#     ['*', '1','*', '1','*', '2','*', '1','*', '1', '*', '2']
#     ], dtype=object)

bars = np.array([
    ['*', '2','*', '2','*', '2','*', '2']
    ])
phrasebars = np.array([
                ['*', '1','*', '1','*', '2','*', '4'],
                ['*', '3','*', '1','*', '2','*', '2'],
                ['*', '1','*', '3','*', '2','*', '2']
                ])

phrase = ''
Nphrasebars = 3 # No. bars in the phrase -1
noteprev = 0
noteprev2 = np.random.randint(0,2)-1 # Determines whether to start going up or down
updownweight = 20
Dup = np.zeros([24,24])
for i in range(24):
    for j in range(24):
        if i == 23 and j == 23:
            Dup[i][j] = 1/100
        elif i == j:
            Dup[i][j] = 1/10
        else:
            Dup[i][j] = 1/(abs(i-j)+1.4)
        if i>j:
            Dup[i][j] /= updownweight
        elif i<j:
            Dup[i][j] *= updownweight
    s = np.sum(Dup[i])
    Dup[i] /= s

Ddown = np.zeros([24,24])
for i in range(24):
    for j in range(24):
        if i == 0 and j == 0:
            Ddown[i][j] = 1/100
        elif i == j:
            Ddown[i][j] = 1/10
        else:
            Ddown[i][j] = 1/(abs(i-j)+1.4)
        if i>j:
            Ddown[i][j] *= updownweight
        elif i<j:
            Ddown[i][j] /= updownweight
    s = np.sum(Ddown[i])
    Ddown[i] /= s

def nextphrase(note, chord):
    #element wise multiply and normalize
    global noteprev2
    global noteprev
    global k
    if k != 0:
        M = np.multiply(np.multiply(N[note],Dup[note]),C[chord])
    else:
        M = np.multiply(np.multiply(N[note],Ddown[note]),C[chord])
    s = np.sum(M)
    M /= s

    r = np.random.rand()
    j = -1
    s = 0
    while s < r:
        j = j + 1
        s = s + M[j]
    noteprev2 = noteprev
    noteprev = j
    return j

k = 0
chord = np.random.randint(0,len(chords))
note = nextphrase(np.random.randint(0, len(notes)), chord)
note1 = note
while k < Nphrasebars:
#    phrasebar = phrasebars[np.random.randint(0,len(phrasebars))]
    phrasebar = phrasebars[k]
    n = len(phrasebar)
    newbar = '|'+'"'+chords[chord]+'"'
    for j in range(0, n):
        if phrasebar[j] != '*':
            newbar = newbar + phrasebar[j]
        else:
            if k == Nphrasebars-1 and j == n-3:
                newbar = newbar + notes[note]
                note = nextphrase(note1, chord)
            else:
                newbar = newbar + notes[note] 
                note = nextphrase(note, chord)
    newbar = newbar + ' '
    phrase = phrase + newbar
    if k == 0:
        firstbar = newbar
    k += 1
    if k == Nphrasebars:
        phrase = phrase + firstbar

    # the last chord should be C
    if k + 4 > Nphrasebars and chord == "0":
        break
    else:
        #loop chords in same order
        chord = (chord+1)%4

print("Fras: " + phrase)

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
    M = np.multiply(np.multiply(N[note],D[note]),C[chord])
    s = np.sum(M)
    M /= s

    r = np.random.rand()
    j = -1
    s = 0
    while s < r:
        j = j + 1
        s = s + M[j]
    return j

tune = ''

k = 0
chord = np.random.randint(0,len(chords))
note = next(np.random.randint(0, len(notes)), chord)

while k < Nbars:
    bar = bars[np.random.randint(0,len(bars))]
    if np.random.randint(0,10) == 1:
        tune = tune + phrase
    n = len(bar)
    newbar = '|'+'"'+chords[chord]+'"'
    for j in range(0, n):
        if bar[j] != '*':
            newbar = newbar + bar[j]
        else:
            newbar = newbar + notes[note] 
            note = next(note, chord)
    
    newbar = newbar + ' '
    tune = tune + newbar
    k += 1

    # the last chord should be C
    if k + 4 > Nbars and chord == "0":
        break
    else:
        #loop chords in same order
        chord = (chord+1)%4

tune = tune + phrase
tune = tune + '|\n'
f.write(tune)
f.close()

from music21 import converter
s = converter.parse('out.abc')
s.write('midi', fp = 'out.mid')
