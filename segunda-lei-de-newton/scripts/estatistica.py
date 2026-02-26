import math

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

  return math.sqrt(aux/(len(tempos)-1))

def errest(tempos):                 # Erro estatístico.
  return desvpad(tempos)/math.sqrt(len(tempos))

def errtot(tempos, errinst):        # Erro total.
  return math.sqrt(errest(tempos)**2+errinst**2)

def prpinc(comp, tempos, errinst):  # Propagação de erros.
  return math.sqrt( (errest(tempos) * comp/media(tempos)**2)**2 + (errinst/media(tempos))**2 )
  

mddinst = {              
# 'Instrumento':[medida(cm), incerteza(cm)],
  'Fotogate':   [0         , 1/1000   ],
  'Paquímetro': [9.75      , 1/200    ],
  'Régua':      [10        , 1/20     ],
}
