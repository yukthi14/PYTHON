import random
print("*** SNAKE - WATER - GUN ***")
def GameWin(Comp,You):
    if Comp==You:
        return None
    elif Comp =='s':
        if You =='w':
            return False
        elif You =='g':
            return True
    elif Comp =='w':
        if You =='g':
            return False
        elif You=='s':
            return True
    elif Comp =='g':
        if You =='s':
            return False
        elif You=='w':
            return True

print("COMPUTER TURN: SNAKE(s) WATER(w) GUN(g)")
randNo=random.randint(1,3)

if randNo == 1:
    Comp ='s'
elif randNo == 2:
    Comp='w'
elif randNo ==3:
    Comp='g'
You=input("YOUR TURN: SNAKE(s) WATER(w) GUN(g) : ")
a= GameWin(Comp,You)

print(f"COMPUTER CHOSE = {Comp}")
print(f"YOU CHOSE = {You}")


if a==None:
    print("!!ITS A TIE!!")
elif a:
    print("!!!!YOU WIN!!!!")
else:
    print("!YOU LOSE!")