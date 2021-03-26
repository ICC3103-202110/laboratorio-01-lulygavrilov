import random

#solicitar el número de cartas a jugar
#una carta es un número
#si los jugadores quieren jugar 20 cartas, 
#debe generar 20 pares con numeros del 1 al 20

#Cada jugador inicia con 0 puntos

print(". : ¡Let's play Memorize! : .")
size = int(input("With how many cards would you like to play?:"))

def board(size):
  board = []
  censor = []
  for i in range (1,size+1):
    board.append(i)
    board.append(i)
    random.shuffle(board)
    censor.append('X ')
    censor.append('X ')
  return censor

print (board(size))