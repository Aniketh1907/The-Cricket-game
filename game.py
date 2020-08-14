import random
import utils


    
#welcome into the game
print("")
print("The Cricket Game")
print("")
#asking player to input his name
print("")
player_name = input("Enter your name:")
print("")
generate_target = utils.computer_target(player_name)
print(""+str(generate_target))
score =0
while generate_target > score:
    num = int(input("Enter number from (0-6): "))
    if utils.validating(num):
        comp_gen = random.randint(0,6)
        if comp_gen==num:
            print("Out")
            print("")
            print(""+str(score))
            break
        else:
            print("")
            
            score = score+num
            print("")
            print("Your score: "+str(score))
            
    else:
        print("Enter a valid number!")
if score>generate_target:
    print(player_name+" you won,waiting for party")
elif score==generate_target:
    print(player_name+" it is Draw")
else:
    print(player_name+" you lost,better luck next time")