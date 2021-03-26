import random

#Beggining of the game

print("\n . : ¡Let's play Memorize! : . \n")

size = int(input("- How many cards would you like to play with? -: "))
while size <0:
    print("- Please enter a valid number-")
    size = int(input("-How many cards would you like to play with?-"))

cardsup = []
cardsdown = []
for i in range (1,size+1):
    cardsup.append(i)
    cardsup.append(i)
    random.shuffle(cardsup)
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

print(cardsup)
print("\n. : Perfect! Lets begin. : . \n . : This is your board : .\n")
display(board(size,cardsdown))
display(board(size,cardsup))

scorep1 = 0
scorep2 = 0

keep_playing = 0 #Loop condition for the game

while keep_playing == 0:
    a = '1'
    coords = input("\n-Player " + a + " select your card's coordinates 'NºRow,NºColumn'. \n(Example: (0,0) for the first card on the top left corner)-: ")
    n = int(coords[0])+1
    m = int(coords[2])
    x = (len(board(size,cardsdown)[0]))
    y = (m*x)-x +n
    print(y)
    cardsdown[y] = cardsup[y]
    display(board(size,cardsdown))

    display(board(size,cardsdown))



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


