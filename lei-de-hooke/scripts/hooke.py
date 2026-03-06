#!/usr/bin/python

import math
import estatistica as est

M = [0.03022, 0.05034, 0.0705, 0.09002]
g = 9.78


D = [
  [.017, .015, .017],
  [.015, .014, .014],
  [.035, .036, .034],
  [.045, .044, .045],
]

M = [0.0302, 0.05034, 0.07005, 0.09002]

def properr(d, m):
   return est.media(d)*m

STAT = []
for d in D:
  STAT.append([est.media(d), est.desvpad(d), est.errest(d), properr(d, M[D.index(d)])])
  


P = []
for m in M:
  P.append([g*m, est.media(D[M.index(m)])])

for stat in STAT:
  print(stat) 
  print(P[STAT.index(stat)])
  print('')



