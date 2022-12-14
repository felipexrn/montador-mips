from limpar import limpa_dois_pontos

def indexar(linhas): # recebe lista de linhas do programa
  listar(linhas) 
  apagar_vazio(linhas) 
  unir_rotulo(linhas)
  rotular(linhas)
  for i in range(len(linhas)): # indexa linhas do programa
    linhas[i] = [linhas[i][0]] + [linhas[i][1:]] + [i]  
  return linhas # retorna linhas rotuladas e indexadas
  
def listar(linhas): # lista linhas quebrando por separador
  for i in range(len(linhas)):
    linhas[i] = linhas[i].split()
    
def unir_rotulo(linhas): # une rótulo solitário com a próxima instrução
  indice = 0
  tamanho = len(linhas)
  while(tamanho > 0):
    if len(linhas[indice]) == 1: 
      if linhas[indice][0].count(":") > 0:
        linhas[indice] += linhas[indice +1]
        del linhas[indice +1]
        indice -= 1
    indice += 1
    tamanho -= 1
    
def rotular(linhas): 
  for i in range(len(linhas)): # rotula instruções
    if linhas[i][0].count(":") == 0:
      linhas[i] = [""] + linhas[i]
    else:
      linhas[i][0] = limpa_dois_pontos(linhas[i][0])

def apagar_vazio(linhas): # apaga linhas vazias
  indice = 0
  tamanho = len(linhas)
  while(tamanho > 0):
    if len(linhas[indice]) == 0:
      del linhas[indice]
      indice -= 1
    indice += 1
    tamanho -= 1

def pega_indice(linhas, valor): # recebe lista de linhas e valor a ser procurado
  for i in range(len(linhas)):
    if linhas[i][0] == valor:
      valor = linhas[i][-1]
  return valor # retorna indice linha que contém do valor

