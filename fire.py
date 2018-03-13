import random 
from random import randint
player = input("ENTER fire(f) log(l) and water(w) ?\n")
print(player,"vs")
choose = randint(1,3)
print(choose)

if choose == 1:
	computer = 'f'
elif choose == 2:
	computer = 'l'
elif choose == 3:
	computer ='w'
else:
	print(" YOU HAVE ENTERED WRONG CHOICE\n")
print(computer)
print(player,"  vs  ",computer)

if player == computer:
	print("DRAW!!")
elif player == 'f' and computer == 'w':
	print("Player Wins")
elif player == 'f' and computer == 'l':
 	print("Computer wins")
elif player == 'f' and computer == 'l':
	print("Player wins")
elif player == 'l' and computer == 'w':
	print("Player wins")
elif player == 'l' and computer == 'f':
	print("Computer wins")
elif player == 'w' and computer == 'f':
	print("Player wins")
elif player == 'w' and computer == 'l':
	print("Computer wins")
else:
	print("Wrong Choice entered ")

