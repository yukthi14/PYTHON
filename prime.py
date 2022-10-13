from operator import truediv


num=int(input("enter the number:\n"))
prime=True
for i in range(2,num):
    if(num%i==0):
        prime=False 
        break
if prime:
    print("this no is prime")
else:
    print("it is prime")