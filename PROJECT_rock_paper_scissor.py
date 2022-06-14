import random
randomNo = random.randint(1,3)
def gameprocessor(comp,you):
    if comp == you:
        return None
    # Check for all possibilities when computer choose Rock

    elif comp == "Rock":
        if you == "Paper":
            return True
        elif you == "Scissor":
            return False
    # Check for all possibilities when computer choose Paper

    elif comp == "Paper":
        if you == "Rock":
            return False
        elif you == "Scissor":
            return True
    # Check for all possibilities when computer choose Scissors

    elif comp == "Scissor":
        if you == "Rock":
            return True
        elif you == "Paper":
            return False


print("Computer's turn: Rock | Paper | Scissor")
if randomNo == 1:
    comp = "Rock"
elif randomNo == 2:
    comp = "Paper" 
elif randomNo == 3:
    comp = "Scissor"

you = input("Your turn: Rock | Paper | Scissor ?\n")

a = gameprocessor(comp,you)
print(f"Computer chose:{comp}")
print(f"You chose:{you}")
if a == None:
    print("Its a Tie")
elif a:
    print("You win")
else:
    print("You lose")    
