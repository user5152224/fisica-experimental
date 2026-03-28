#!/usr/bin/python

import math
import estatistica as est

L = [                                                 # Lista de comprimentos para cada modos
  # 1     2     3      modos
  [ .123, .245, .363], # 60g 
  [ .175, .351, .530], # 110g
  [ .211, .424, .635], # 160g
  [ .250, .498, .745], # 210g
  [ .283, .556, .855], # 260g
]

LAMBD = [
  [2*l/(lens.index(l)+1) for l in lens] for lens in L # Dupla compreensão de listas (lista dos lambdas)
]          
EE    = [est.errest(lambd) for lambd in LAMBD]        # Compreensão de erros estatísticos (lista dos erros est.)
g     = 9.78                                          # Aceleração gratitacional próximo à superfície terrestre
M     = [.060, .110, .160, .210, .260]                # Sequência de massas usadas
T     = [g*m for m in M]                              # Compreensão de lista de pesos (Módulo da força peso)

for lambd in LAMBD:
    print(f'{est.media(lambd)} ± {est.errest(lambd)}')

