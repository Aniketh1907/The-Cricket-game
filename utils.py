import random

#creating a function computer_target 
def computer_target(name):
#assigning a random number which is generated by random module to comp variable
    comp = random.randint(11,100)
    print(name+" your target is: "+str(comp))
    return comp

def validating(hand):
    if hand<1 or hand>6:
        return False
    else:
        return True