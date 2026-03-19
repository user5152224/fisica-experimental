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

