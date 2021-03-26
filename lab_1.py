import random

#Inicio del juego

print("\n . : ¡Let's play Memorize! : . \n")

#Creación del tablero con cartas solicitadas

size = int(input("- With how many cards would you like to play? -: "))
while size <0:
    print("- Please enter a valid number-")
    size = int(input("-With how many cards would you like to play?-"))

cards = []
censor = []
for i in range (1,size+1):
    cards.append(i)
    cards.append(i)
    random.shuffle(cards)
    censor.append('X ')
    censor.append('X ')

def board(size,typeofboard):
  if (size%3) == 0:
      i = 0
      board = []
      while i<len(typeofboard):
          board.append(typeofboard[i:i+3])
          i+=3
  elif(size%5) == 0:
      i = 0
      board =[]
      while i<len(typeofboard):
          board.append(typeofboard[i:i+5])
          i+=5
  return board

def display(board):
    for i in board:
        print(i)

print("\n. : Perfect! Lets begin. : . \n . : This is your board : .\n")
display(board(size,censor))

scorep1 = 0
scorep2 = 0

keep_playing = 0 #Escribimos esto como condición para el loop del juego

while keep_playing == 0:
    a = '1'
    coords1 = input("\n-Player " + a + " select your card's coordinates. (Example: 0,1)-: ")






    condition_to_continue = input("\n- Do you wish to keep playing? <Yes/No> - :")
    if condition_to_continue == 'No' or condition_to_continue == 'no':
        keep_playing = 1
    elif condition_to_continue == 'Yes' or condition_to_continue == 'yes':
        keep_playing = 0
    else:
        print("-The answer was not valid. Play another round and try again!-")

if scorep1 > scorep2:
    print("\n -Player 1 wins by .:" + str(scorep1 - scorep2) + ":. points, with a score of" + str(scorep1) + "!-")
elif scorep1 == scorep2:
    print("\n -¡Its a Draw! You guys matched with .:" + str(scorep1) + ":. points!-")
else:
    print("\n -Player 2 wins by .:" + str(scorep2 - scorep1) + ":. points, with a score of" + str(scorep2) + "!-")

print("\n. : Wohoo what a great game! Thank you for playing please come back soon. : .")


