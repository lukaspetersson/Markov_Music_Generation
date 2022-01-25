from music21 import converter
s = converter.parse('out.abc')
s.write('midi', fp = 'out.mid')
