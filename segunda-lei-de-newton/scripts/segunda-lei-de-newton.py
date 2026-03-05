#!/usr/bin/python

import math
import estatistica as est

T = [
  [.139, .140, .141, .141, .140, .141, .139, .141, .141, .141],
  [.099, .100, .100, .100, .100, .100, .100, .104, .104, .104],
  [.079, .079, .080, .079, .079, .086, .084, .088, .088, .089],
  [.070, .070, .072, .074, .070, .080, .078, .081, .082, .082],
] # segundos

d = 0.0955 # metro

V = []

for tempos in T:
  v = []
  for t in tempos:
    v.append(d/t)

  V.append(v)

D = [.22, .44, .66, .88]
   
for v in V:
  med = est.media(v) 
  ind = V.index(v)
  print(f'       {ind+1}. {D[ind]} {med:6.2f} {math.sqrt(med)}')
