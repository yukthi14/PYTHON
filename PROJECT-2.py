import random
randNumber=random.randint(1,100)
print(randNumber)
userGuess=None
guesses=0
while(userGuess!=randNumber):
    userGuess=int(input("Enter your guess:"))
    guesses +=1
    if(userGuess==randNumber):

        print("You guessed it right !!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong !! enter smaller number")
        else:
            print("You guessed it wrong!!! enter larger number")
        guesses +=1
print(f"You gussed the number in {guesses} gusses")