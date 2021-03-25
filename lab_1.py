import random

#solicitar el número de cartas a jugar
#una carta es un número
#si los jugadores quieren jugar 20 cartas, 
#debe generar 20 pares con numeros del 1 al 20

def board(size):
  board = []
  for i in range (1,size+1):
    board.append(i)
  return board

print(board(20))

print(random.shuffle(board(20)))