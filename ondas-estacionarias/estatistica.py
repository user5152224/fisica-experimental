import math

def media(tempos): # Média aritmética.
  aux = 0 
  for v in tempos:
    aux += v
  return aux/len(tempos)

def desvpad(tempos): # Desvio padrão
  med = media(tempos)
  aux = 0
  for ent in tempos:
    aux += (med - ent)**2

  return math.sqrt(aux/(len(tempos)-1))

def errest(tempos): # Erro estatístico.
  return desvpad(tempos)/math.sqrt(len(tempos))

def somat(v): # Somatória.
  soma = 0
  for coor in v:
    soma += coor

  return soma

def somaquad(v): # Soma dos quadrados.
  soma = 0
  for coor in v:
    soma += coor**2

  return soma

def prodint(u, v): # Produto interno (ou escalar).
  soma = 0
  for i in range(len(u)):
    soma += u[i]*v[i]

  return soma  

def regressao(x, y): # Regressão linear de y em x.
  n   = len(x)
  p   = prodint(x,y)
  q_x = somaquad(x)
  s_x = somat(x)
  s_y = somat(y)
  D   = n*q_x-s_x**2

  A = (s_y*q_x - p*s_x)   / D
  B = (n*p     - s_x*s_y) / D

  return [A, B]

def sigma_y(x, y):
  n    = len(x)
  soma = 0
  C    = regressao(x, y)
  for i in range(len(x)):
    soma += (C[0]+C[1]*x[i]-y[i])**2

  return math.sqrt(soma/(n-2))

def sigma_b(x, y):
  n     = len(x)
  q_x   = somaquad(x)
  s_x   = somat(x)
  sig_y = sigma_y(x, y)

  return sig_y * math.sqrt(n/(n*q_x-s_x**2))
