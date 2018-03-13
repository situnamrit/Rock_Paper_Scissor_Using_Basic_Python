import random 
from random import randint
player = input("ENTER rock(r) paper(p) and scissors(s) ?\n")
print(player,"vs")
choose = randint(1,3)
print(choose)

if choose == 1:
	computer = 'r'
elif choose == 2:
	computer = 'p'
elif choose == 3:
	computer ='s'
else:
	print(" YOU HAVE ENTERED WRONG CHOICE\n")
print(computer)
print(player,"  vs  ",computer)

if player == computer:
	print("DRAW!!")
elif player == 'r' and computer == 's':
	print("Player Wins")
elif player == 'r' and computer == 'p':
 	print("Computer wins")
elif player == 'r' and computer == 's':
	print("Player wins")
elif player == 'p' and computer == 'r':
	print("Player wins")
elif player == 'p' and computer == 's':
	print("Computer wins")
elif player == 's' and computer == 'p':
	print("Player wins")
elif player == 's' and computer == 'r':
	print("Computer wins")
else:
	print("Wrong Choice entered ")

