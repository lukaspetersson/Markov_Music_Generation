import numpy as np


notes = ['C',"^C" ,'D',"^D", 'E', 'F',"^F", 'G',"^G", 'A',"^A", 'B', 'c',"^c", 'd',"^d", 'e', 'f',"^f", 'g',"^g", 'a',"^a", 'b']
chords = ['C', 'G', 'Am', 'F'] 

phrasebars = 3

#markov for notes
N = np.array([[0.1, 0.1, 0.2, 0.1, 0.3, 0.0, 0.0, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0,0,0,0,0,0,0,0,0,0],
              [0.0, 0.1, 0.1, 0.1, 0.3, 0.3, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0,0,0,0,0,0,0,0,0,0],
              [0.1, 0.0, 0.1, 0.1, 0.0, 0.3, 0.3, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0, 0,0,0,0,0,0,0,0,0,0],
              [0.0, 0.1, 0.1, 0.2, 0.0, 0.1, 0.4, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0,0,0,0,0,0,0,0,0,0],
              [0.2, 0.2, 0.0, 0.0, 0.1, 0.1, 0.1, 0.2, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0,0,0,0,0,0,0,0,0,0],
              [0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.0, 0.2, 0.0, 0.0, 0.1, 0.0, 0,0,0,0,0,0,0,0,0,0],
              [0.0, 0.0, 0.1, 0.2, 0.1, 0.1, 0.2, 0.0, 0.1, 0.1, 0.0, 0.0, 0.0, 0.1, 0,0,0,0,0,0,0,0,0,0],
              [0.0, 0.0, 0.1, 0.2, 0.1, 0.1, 0.2, 0.0, 0.1, 0.1, 0.0, 0.0, 0.0, 0.1, 0,0,0,0,0,0,0,0,0,0],
              [0.0, 0.0, 0.1, 0.2, 0.1, 0.1, 0.2, 0.0, 0.1, 0.1, 0.0, 0.0, 0.0, 0.1, 0,0,0,0,0,0,0,0,0,0],
              [0.0, 0.0, 0.1, 0.2, 0.1, 0.1, 0.2, 0.0, 0.1, 0.1, 0.0, 0.0, 0.0, 0.1, 0,0,0,0,0,0,0,0,0,0],
              [0.0, 0.0, 0.1, 0.2, 0.1, 0.1, 0.2, 0.0, 0.1, 0.1, 0.0, 0.0, 0.0, 0.1, 0,0,0,0,0,0,0,0,0,0],
              [0.0, 0.0, 0.1, 0.2, 0.1, 0.1, 0.2, 0.0, 0.1, 0.1, 0.0, 0.0, 0.0, 0.1, 0,0,0,0,0,0,0,0,0,0],
              [0.0, 0.0, 0.1, 0.2, 0.1, 0.1, 0.2, 0.0, 0.1, 0.1, 0.0, 0.0, 0.0, 0.1, 0,0,0,0,0,0,0,0,0,0],
              [0.0, 0.0, 0.1, 0.2, 0.1, 0.1, 0.2, 0.0, 0.1, 0.1, 0.0, 0.0, 0.0, 0.1, 0,0,0,0,0,0,0,0,0,0],
              [0.0, 0.0, 0.1, 0.2, 0.1, 0.1, 0.2, 0.0, 0.1, 0.1, 0.0, 0.0, 0.0, 0.1, 0,0,0,0,0,0,0,0,0,0],
              [0.0, 0.0, 0.1, 0.2, 0.1, 0.1, 0.2, 0.0, 0.1, 0.1, 0.0, 0.0, 0.0, 0.1, 0,0,0,0,0,0,0,0,0,0],
              [0.0, 0.0, 0.1, 0.2, 0.1, 0.1, 0.2, 0.0, 0.1, 0.1, 0.0, 0.0, 0.0, 0.1, 0,0,0,0,0,0,0,0,0,0],
              [0.1, 0.0, 0.0, 0.0, 0.1, 0.1, 0.0, 0.1, 0.1, 0.2, 0.1, 0.2, 0.0, 0.0, 0,0,0,0,0,0,0,0,0,0],
              [0.0, 0.1, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.0, 0,0,0,0,0,0,0,0,0,0],
              [0.0, 0.0, 0.1, 0.0, 0.0, 0.1, 0.0, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.0, 0,0,0,0,0,0,0,0,0,0],
              [0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3, 0,0,0,0,0,0,0,0,0,0],
              [0.0, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.1, 0.2, 0.2, 0.0, 0.2, 0.1, 0.1, 0,0,0,0,0,0,0,0,0,0],
              [0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.2, 0.2, 0.1, 0.1, 0.2, 0.1, 0,0,0,0,0,0,0,0,0,0],
              [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.0, 0.0, 0.1, 0.4, 0.1, 0.1, 0.1, 0,0,0,0,0,0,0,0,0,0]])

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

updownweight = 20
Dup = np.zeros([24,24])
for i in range(24):
    for j in range(24):
        if i == j:
            Dup[i][j] = 1/50
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
        if i == j:
            Ddown[i][j] = 1/50
        else:
            Ddown[i][j] = 1/(abs(i-j)+1.4)
        if i>j:
            Ddown[i][j] *= updownweight
        elif i<j:
            Ddown[i][j] /= updownweight
    s = np.sum(Ddown[i])
    Ddown[i] /= s

f = open("phrase.abc", "w")

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

noteprev = 0
noteprev2 = np.random.randint(0,2)-1

def nextphrase(note, chord):
    #element wise multiply and normalize
    global noteprev2
    global noteprev
    if noteprev - noteprev2 > 0:
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

bar = ['*', '2','*', '2','*', '4']
phrase = ''

k = 0
chord = np.random.randint(0,len(chords))
note = nextphrase(np.random.randint(0, len(notes)), chord)
note1 = note
while k < phrasebars:
    n = len(bar)
    newbar = '|'+'"'+chords[chord]+'"'
    for j in range(0, n):
        if bar[j] != '*':
            newbar = newbar + bar[j]
        else:
            if k == phrasebars-1 and j == n-3:
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
    if k == phrasebars:
        phrase = phrase + firstbar

    # the last chord should be C
    if k + 4 > phrasebars and chord == "0":
        break
    else:
        #loop chords in same order
        chord = (chord+1)%4

print(phrase)
phrase = phrase + '|\n'

f.write(phrase)
f.close()

from music21 import converter
s = converter.parse('phrase.abc')
s.write('midi', fp = 'phrase.mid')
