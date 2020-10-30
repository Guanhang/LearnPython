import random

player = int(input("你要出的是 石头 (1) /剪刀 (2) /布 (3) : "))

computer = random.randint(1,3)

print("the player choice is %d - the computer choice is %d" % (player, computer))

if ((player == 1 and computer == 2) 
        or (player == 2 and computer == 3) 
        or (player == 3 and computer == 1)):
        
    print("Player Win")
    
elif player == computer:
    print("Again")

else:
    print("Player lose")
