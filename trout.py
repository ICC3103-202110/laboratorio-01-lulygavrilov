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


coords = input("\n-Player  select your card's coordinates. \n(Example: 0,0 for the first card on the top left corner)-: ")
n = int(coords[0])+1
m = int(coords[2])
x = (len(board(size,cardsdown)[0]))-1
y = (m*x)+n
print(y)
