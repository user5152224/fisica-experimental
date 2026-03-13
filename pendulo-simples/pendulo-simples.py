#!/usr/bin/python

import math
import estatistica as est

T = [
  [11.62, 11.78, 11.50, 11.85, 11.76],
  [16.15, 16.19, 15.72, 15.87, 16.19], #3
  [17.96, 17.67, 17.64, 17.47, 17.88], #4
  [18.72, 19.20, 19.10, 18.83, 19.05],
] # segundos

for tempos in T:
    print(f"{est.media(tempos):.4f} {est.media(tempos):.4f} {est.errest(tempos):.1f} ")
