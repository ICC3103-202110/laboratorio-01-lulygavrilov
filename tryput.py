import random

size = 20

cardsup = []
cardsdown = []
for i in range (1,size+1):
    cardsup.append(i)
    cardsup.append(i)
    cardsdown.append('X ')
    cardsdown.append('X ')

random.shuffle(cardsup)

print(cardsup)

def boardcardsup(size):
  divisibility = [2,3,5]
  for j in divisibility:
    if (size%j) == 0:
        i = 0
        board = []
        while i<len(cardsup):
            board.append(cardsup[i:i+j])
            i+=j  
  return board

def boardcardsdown(size):
   divisibility = [2,3,5]
   for j in divisibility:
    if (size%j) == 0:
        i = 0
        board = []
        while i<len(cardsdown):
            board.append(cardsdown[i:i+j])
            i+=j  
   return board

def display(board):
    for i in board:
        print(i)



print(len(boardcardsdown(size)[0]))