#!/usr/bin/python

import math
import estatistica as est

T = [
  [11.62, 11.78, 11.50, 11.85, 11.76],
  [13.70, 14.35, 14.20, 14.17, 10.03],
  [16.15, 16.19, 15.72, 15.87, 16.19], #3
  [17.96, 17.67, 17.64, 17.47, 17.88], #4
  [18.72, 19.20, 19.10, 18.83, 19.05],
  [20.63, 20.62, 21.17, 20.82, 20.43],
  [21.61, 22.04, 21.47, 21.96, 21.48],
  [23.05, 23.07, 23.66, 23.47, 23.87],
] # segundos

errinst = 0.01

def errtot(tempos):
  ee = est.errest(tempos)

  return math.sqrt(ee**2+errinst**2)

L = [.35, .496, .648, .783, .899, 1.097, 1.193, 1.373]
for tempos in T:
    print(f"Teste {T.index(tempos)+1:2d}: {est.media(tempos):.2f} {est.desvpad(tempos):.3f} {est.errest(tempos):.1f} {errtot(tempos):.2f} ({est.media(tempos)/10:.3f}, {L[T.index(tempos)]}) ({(est.media(tempos)/10)**2:.3f}, {L[T.index(tempos)]})")
