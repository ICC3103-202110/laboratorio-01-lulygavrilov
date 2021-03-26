import random

#Inicio del juego

print("\n . : ¡Let's play Memorize! : . \n")

#Creación de/los mazos (cartas boca arriba y boca abajo(censuradas))

size = int(input("- With how many cards would you like to play? -: "))
while size <0:
    print("- Please enter a valid number-")
    size = int(input("-With how many cards would you like to play?-"))

cardsup = []
cardsdown = []
for i in range (1,size+1):
    cardsup.append(i)
    cardsup.append(i)
    cardsdown.append('X ')
    cardsdown.append('X ')


def board(size,typeofcard):
  divisibility = [2,3,5]
  for j in divisibility:
    if (size%j) == 0:
        i = 0
        board = []
        while i<len(typeofcard):
            board.append(typeofcard[i:i+j])
            i+=j  
  return board

def display(board):
    for i in board:
        print(i)

print("\n. : Perfect! Lets begin. : . \n . : This is your board : .\n")
display(board(size,cardsdown))

scorep1 = 0
scorep2 = 0

keep_playing = 0 #Escribimos esto como condición para el loop del juego

while keep_playing == 0:
    a = '1'
    coords = input("\n-Player " + a + " select your card's coordinates. \n(Example: 0,0 for the first card on the top left corner)-: ")
    n = int(coords[0])
    m = int(coords[2])
    board(size,cardsdown)[n][m] = board(size,cardsup)[n][m]
    print(display(board(size,cardsdown)))



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


