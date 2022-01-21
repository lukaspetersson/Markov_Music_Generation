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

Nbars = 30

M = np.zeros((Nnotes, Nnotes))
M[0, 1] = 0.3
M[0, 2] = 0.7
M[1, 0] = 0.2
M[1, 2] = 0.2
M[1, 3] = 0.6

for k in range(2, Nnotes - 2):
    M[k, k - 2] = 0.3
    M[k, k - 1] = 0.2
    M[k, k + 1] = 0.2
    M[k, k + 2] = 0.3

M[Nnotes - 1, Nnotes - 2] = 0.3
M[Nnotes - 1, Nnotes - 3] = 0.7
M[Nnotes - 2, Nnotes - 1] = 0.2
M[Nnotes - 2, Nnotes - 3] = 0.2
M[Nnotes - 2, Nnotes - 4] = 0.6


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

bars = [['(', '*', '3', ' ', '*', ')', '*', '*'],
        ['*', '4', ' ', '*', '2'],
        ['*', '3', ' ', '*', '*', '2'],
        ['*', '2', ' ', '(', '*', '*', '*', '*', ')']]

N = np.array([[0.5, 0.2, 0.2, 0.1],
              [0.5, 0, 0.2, 0.3],
              [0.5, 0.2, 0, 0.3],
              [0.6, 0.1, 0.1, 0.2]])
startbar = 0
endbar = 1
stopBar = ['z2 ', '*', '2', '*', '2', ' | ', 'z2 ', '*', '4']

print('%%abc-charset utf-8')
print('%%titlefont NewCenturySchlbk-Roman 22')
print('%%subtitlefont NewCenturySchlbk 16')
print('%%composerfont NewCenturySchlbk-Italic 14')
print('%%footerfont NewCenturySchlbk 16')
print('%%headerfont NewCenturySchlbk 16')
print('%%tempofont NewCenturySchlbk-Bold 15')
print('X:1')
print('T:Markovtest')
print('C:strauss (localhost)')
print('L:1/8')
print('M:3/4')
print('R:walz')
# 180=presto, 160=vivace, 132=allegro, 96=moderato, 72=andante
print('Q: "Vivace" 1/4 = 160')
print('V:1')
print('K:C')
print('%%MIDI channel 1')
#print('%%MIDI program 1 48') # strängar
#print('%%MIDI program 1 0') # piano
print('%%MIDI program 1 22')
print('%%MIDI chordprog 0')
print('%%MIDI chordvol 40')
print('%%MIDI drum ddd 60 61 61 50 40 40')
print('%%MIDI drumon')

bar = startbar
Bar = bars[bar]
note = startnote
tune = ''

k = -1
while k < Nbars:
    k = k + 1
    n = len(Bar)
    newbar = '| '
    if note == 0 or note == 7:
        newbar = newbar + '"C"'
    if note == 1 or note == 8:
        newbar = newbar + '"D"'
    if note == 2 or note == 9:
        newbar = newbar + '"E"'    
    if note == 3 or note == 10:
        newbar = newbar + '"F"'
    if note == 4 or note == 11:
        newbar = newbar + '"G"'
    if note == 5 or note == 12:
        newbar = newbar + '"A"'
    if note == 6 or note == 13:
        newbar = newbar + '"B"'
        
    for j in range(0, n):
        if Bar[j] != '*':
            newbar = newbar + Bar[j]
        else:
            newbar = newbar + notes[note]
            note = next(note, M)

    if k > Nbars - 1:
        if bar != endbar:
            k = Nbars - 1

    bar = next(bar, N)
    Bar = bars[bar]
    
    newbar = newbar + ' '
    tune = tune + newbar

Bar = stopBar
n = len(Bar)
newbar = '| '
for j in range(0, n):
    if Bar[j] != '*':
        newbar = newbar + Bar[j]
    else:
        newbar = newbar + notes[note]
        note = next(note, M)
newbar = newbar + ' '
tune = tune + newbar

tune = tune + '|'

print(tune)
