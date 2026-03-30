#!/usr/bin/env python

import math
import estatistica as est

L = [ # Lista de comprimentos (em metro) para cada modo.
      # modos   1     2     3 
              [.123, .245, .363], # 60g 
              [.175, .351, .530], # 110g
              [.211, .424, .635], # 160g
              [.250, .498, .745], # 210g
              [.283, .556, .855], # 260g
]

LA      = [[2*l/(lens.index(l)+1) for l in lens] for lens in L ] # Lista dos lambdas.          
MED     = [est.media(lambd) for lambd in LA]                     # Lista de médias.
QUADMED = [med**2 for med in MED]                                # Quadrado das médias para regressão.
ERREST  = [est.errest(lambd) for lambd in LA]                    # Erros estatísticos.
g       = 9.78                                                   # Aceleração gratitacional estipulada (m/s^2)
MASSAS  = [.060, .110, .160, .210, .260]                         # Massas usadas (em Kg).
T       = [g*m for m in MASSAS]                                  # Trações (módulo da força peso).
C       = est.regressao(T, QUADMED)                              # Regressao (y=A+Bx), leia-se [A, B].

print(f'x     y')
for t in T:
  print(f'{t:.3f} {QUADMED[T.index(t)]:.7f}')

print('')

print(C)
print(est.sigma_b(T, QUADMED)/(C[1]*120)**2)
#00001.288400723039702e


