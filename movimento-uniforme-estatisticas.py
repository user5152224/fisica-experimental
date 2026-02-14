#!/usr/bin/python

from math import *

# matriz temporal
T = [
       [ .264, .264, .262, .262, .257, .264, .267, .269, .259, .267 ],
       [ .267, .268, .267, .266, .260, .269, .271, .272, .262, .269 ],
       [ .272, .273, .271, .270, .264, .273, .275, .278, .267, .275 ],
       [ .275, .276, .273, .272, .267, .274, .272, .278, .267, .275 ],
    ]

def media(tempos):                  # Média aritmética.
  aux = 0 

  for v in tempos:
    aux += v

  return aux/len(tempos)

def desvpad(tempos):                # Desvio padrão
  med = media(tempos)
  aux = 0

  for ent in tempos:
    aux += (med - ent)**2

  return sqrt(aux/(len(tempos)-1))

def errest(tempos):                 # Erro estatístico.
  return desvpad(tempos)/sqrt(len(tempos))

def errtot(tempos, errinst):        # Erro total.
  return sqrt(errest(tempos)**2+errinst**2)

def prpinc(comp, tempos, errinst):  # Propagação de erros.
  return sqrt( (errest(tempos) * comp/media(tempos)**2)**2 + (errinst/media(tempos))**2 )
  

mddinst = {              
# 'Instrumento':[medida(cm), incerteza(cm)],
  'Fotogate':   [0         , 1/1000   ],
  'Paquímetro': [9.75      , 1/200    ],
  'Régua':      [10        , 1/20     ],
}

cabecalho = [
  '       ',
  'Instrumento',
  'Tempo médio',
  'Desvio padrão',
  'Erro total',
  'Velociada média',
  'Propagação de erros',
  'Intervalo de incerteza'
]

print(f'{cabecalho[0]}   {cabecalho[1]}   {cabecalho[2]}   {cabecalho[3]}   {cabecalho[4]}   {cabecalho[5]}   {cabecalho[6]}   {cabecalho[7]}')
for inst in ['Régua', 'Paquímetro']:
  print(f'{cabecalho[0]}   {inst:>{len(cabecalho[1])}}')
  for tempos in T:
    tempo_medio            = media(tempos)
    desvio_padrao          = desvpad(tempos)
    erro_total             = errtot(tempos, mddinst['Fotogate'][0])
    velocidade_media       = mddinst[inst][0]/tempo_medio
    propagacao_de_erros    = prpinc(mddinst[inst][0], tempos, mddinst[inst][1]) 
    intervalo_de_incerteza = f'[{velocidade_media-propagacao_de_erros:.1f},{velocidade_media+propagacao_de_erros:.1f}]'

    print(f'{cabecalho[0]:{len(cabecalho[0]+cabecalho[1])}}      ', end='')
    print(f'{tempo_medio:{len(cabecalho[2])}.2f}   '              , end='')
    print(f'{desvio_padrao:{len(cabecalho[3])}.3f}   '            , end='')
    print(f'{erro_total:{len(cabecalho[4])}.3f}   '               , end='')
    print(f'{velocidade_media:{len(cabecalho[5])}.1f}   '         , end='')
    print(f'{propagacao_de_erros:{len(cabecalho[6])}.1f}   '      , end='')
    print(f'{intervalo_de_incerteza:>{len(cabecalho[7])}}')

