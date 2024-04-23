import time
import os

vetor = []

def add():
  print("No momento, o vetor é:",vetor)
  op = "1"
  while op == "1":
    vetor.append(int(input("Digite um número inteiro: ")))
    op = input("DESEJA DIGITAR OUTRO NÚMERO? '1' P/ SIM, '2' P/ NÃO: ")

  print("VETOR CRIADO:",vetor)
  print("O VETOR CRIADO POSSUI", len(vetor), "POSIÇÕES")
  time.sleep(3)
  os.system('cls')

def pesq():
  print("No momento, o vetor é:",vetor)
  v_procurado = int(input("Digite um valor a ser procurado: "))
  print("Procurando o valor",v_procurado,"no vetor",vetor)
  for i in range(len(vetor)):
    if v_procurado == vetor[i]:
      print("Valor encontrado no índice",i)
    else:
      print("Valor não encontrado no índice",i)
  time.sleep(3)
  os.system('cls')

def alt():
  print("No momento, o vetor é:",vetor)
  v_procurado = int(input("Digite um valor a ser procurado: "))
  posicao = 0
  for i in range(len(vetor)):
    if v_procurado == vetor[i]:
      posicao = vetor.index(v_procurado)
      print("O valor procurado está na posição",posicao)
      print(vetor[posicao])
  vetor[posicao] = int(input("Digite um novo valor para a posição:"))
  print(vetor)
  time.sleep(3)
  os.system('cls')

def dele():
  print("No momento, o vetor é:",vetor)
  j = 0
  j = int(input("Digite o índice para removê-lo do vetor: "))
  del vetor[j]
  print(vetor)
  time.sleep(3)
  os.system('cls')

menu = 1

while menu:
  print("1. Criar um vetor")
  print("2. Pesquisar um dado no vetor")
  print("3. Alterar um dado no vetor")
  print("4. Deletar um dado do vetor")
  print("0. Sair")
  menu = int(input("Escolha uma opção:"))

  if(menu==1):
    add()
  if(menu==2):
    pesq()
  if(menu==3):
    alt()
  if(menu==4):
    dele()