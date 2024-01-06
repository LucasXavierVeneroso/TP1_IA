#Classe para nó da árvore de estados
class Node:
  def __init__(self,vector,cost,heuristic,nav_cost,father):
    self.vector = vector
    self.cost = cost
    self.heuristic = heuristic
    self.nav_cost = nav_cost
    self.father = father

#Funçao de expandir um nó
def expandNode(v,s):
  h = 0
  s = []
  for i in range(len(v.vector)):
    for j in range(i+1,len(v.vector)):
      if v.vector[i] > v.vector[j]:
        newNode = v.vector.copy()
        aux = newNode[i]
        newNode[i] = newNode[j]
        newNode[j] = aux
        if j - i == 1:
          cost = 2
        else:
          cost = 4
        for k in range(len(newNode)):
          if newNode[k] != k+1:
            h += 1
        n = Node(newNode,cost,h,v.nav_cost + cost,v)
        s.append(n)
        h = 0
  return s

#Funçao para imprimir os intermediários
def printIntermidiate(vector):
  i = vector[len(vector)-1]
  exp_tree = []
  exp_tree.append(i)
  
  while i.father != 0:
    i = i.father
    exp_tree.append(i)
    
  for j in range(len(exp_tree)):
    print(exp_tree.pop().vector)

#BFS
def doBFS(vector,inter):
  n0 = Node(vector,0,0,0,0)
  frontier = [n0]
  
  for i in range(len(vector)):
    if vector[i] != i+1:
      frontier[0].heuristic += 1
  
  solution = 0
  explored = []
  n_expansions = 0
  repeat = 0 

  while solution == 0:
    aux_vector = frontier.pop(0)
    for i in range(len(explored)):
      if aux_vector.vector == explored[i].vector:
        repeat = 1
    if repeat == 0:
      explored.append(aux_vector)
      frontier.extend(expandNode(aux_vector,frontier))
      n_expansions += 1
      if aux_vector.heuristic == 0:
        solution = 1
        break
    repeat = 0

  print(explored[len(explored)-1].nav_cost,n_expansions)

  if inter == True:
    printIntermidiate(explored)

#IDS
def recursiveIDS(f,e,n_exp,i,d,r):
  aux_vector = f.pop(0)
  n_expansion_level = 0
  if i == d:
    return 0
  repeat = 0
  if r == 0:    
    for j in range(len(e)):
      if aux_vector.vector == e[j].vector:
        repeat = 1
    if repeat == 0:
      e.append(aux_vector)
      aux_f = expandNode(aux_vector,f)
      n_expansion_level = len(aux_f)
      aux_f.extend(f)
      f = aux_f
      n_exp.append(1)
      if aux_vector.heuristic == 0:
        return 1
    repeat = 0
    n = 0
    while n < n_expansion_level and r == 0:
      r = recursiveIDS(f,e,n_exp,i+1,d,r)
      n += 1
    if i == 0:
      return r,e
    else:
      return r

def doIDS(vector,inter):
  n0 = Node(vector,0,0,0,0)
  frontier = [n0]
  n_exp_IDS = []
  for i in range(len(vector)):
    if vector[i] != i+1:
      frontier[0].heuristic += 1
  s = 0
  depth_of_tree = 0
  while s == 0:
    depth_of_tree += 1
    s,explored = recursiveIDS(frontier.copy(),[],n_exp_IDS,0,depth_of_tree,s)

  print(explored[len(explored)-1].nav_cost,len(n_exp_IDS))
  
  if inter == True:
    printIntermidiate(explored)

#UCS
def doUCS(vector,inter):
  n0 = Node(vector,0,0,0,0)
  frontier = [n0]
  
  for i in range(len(vector)):
    if vector[i] != i+1:
      frontier[0].heuristic += 1
  
  solution = 0
  explored = []
  n_expansions = 0
  repeat = 0 

  while solution == 0:
    aux_vector = frontier.pop(0)
    for i in range(len(explored)):
      if aux_vector.vector == explored[i].vector:
        repeat = 1
    if repeat == 0:
      explored.append(aux_vector)
      frontier.extend(expandNode(aux_vector,frontier))
      frontier.sort(key = lambda a: a.nav_cost)
      n_expansions += 1
      if aux_vector.heuristic == 0:
        solution = 1
        break
    repeat = 0
  
  print(explored[len(explored)-1].nav_cost,n_expansions)
  
  if inter == True:
    printIntermidiate(explored)

#A*
def doASTAR(vector,inter):
  n0 = Node(vector,0,0,0,0)
  frontier = [n0]
  
  for i in range(len(vector)):
    if vector[i] != i+1:
      frontier[0].heuristic += 1
  
  solution = 0
  explored = []
  n_expansions = 0
  repeat = 0 

  while solution == 0:
    aux_vector = frontier.pop(0)
    for i in range(len(explored)):
      if aux_vector.vector == explored[i].vector:
        repeat = 1
    if repeat == 0:
      explored.append(aux_vector)
      frontier.extend(expandNode(aux_vector,frontier))
      frontier.sort(key = lambda a: a.nav_cost + a.heuristic)
      n_expansions += 1
      if aux_vector.heuristic == 0:
        solution = 1
        break
    repeat = 0

  print(explored[len(explored)-1].nav_cost,n_expansions)
  
  if inter == True:
    printIntermidiate(explored)

#Greedy best-first search
def doGreedy(vector,inter):
  n0 = Node(vector,0,0,0,0)
  frontier = [n0]
  
  for i in range(len(vector)):
    if vector[i] != i+1:
      frontier[0].heuristic += 1
  
  solution = 0
  explored = []
  n_expansions = 0
  repeat = 0 

  while solution == 0:
    aux_vector = frontier.pop(0)
    for i in range(len(explored)):
      if aux_vector.vector == explored[i].vector:
        repeat = 1
    if repeat == 0:
      explored.append(aux_vector)
      frontier = expandNode(aux_vector,frontier)
      frontier.sort(key = lambda a: a.heuristic)
      n_expansions += 1
      if aux_vector.heuristic == 0:
        solution = 1
        break
    repeat = 0

  print(explored[len(explored)-1].nav_cost,n_expansions)
  
  if inter == True:
    printIntermidiate(explored)

#Main
entrada = input()
entrada = entrada.split(' ')

tipo_algoritmo = entrada.pop(0)
tam_vetor = int(entrada.pop(0))
vetor = []
intermid = False

for i in range(tam_vetor):
  vetor.append(int(entrada.pop(0)))

if len(entrada) != 0 and entrada.pop(0) == 'PRINT':
  intermid = True

match tipo_algoritmo:
  case 'B':
    doBFS(vetor,intermid)
  case 'I':
    doIDS(vetor,intermid)
  case 'U':
    doUCS(vetor,intermid)
  case 'A':
    doASTAR(vetor,intermid)
  case 'G':
    doGreedy(vetor,intermid)