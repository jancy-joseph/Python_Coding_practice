#!/bin/python3

from random import randint

player = input("rock(r),paper(p),scissors(s)?")
print(player,'vs',end=' ')
chosen = randint(1,3)
#print(chosen)
if(chosen == 1):
  computer = 'r'
elif(chosen == 2):
  computer = 'p'
else:
  computer ='s'
print(computer)
if(player == computer):
  print('DRAW!')
elif(player == 'r' and computer =='s'):
  print("You won!")
elif(player == 'p' and computer == 's'):
  print("Computer Won! Try again")
elif(player =='s' and computer =='p'):
  print("You won!");
elif(player == 'r' and computer =='p'):
  print("you won!")
elif(player=='s' and computer =='r'):
  print("Computer won!.Try again")
elif(player == 'p' and computer =='r'):
  print("Computer Won!.Try again")
