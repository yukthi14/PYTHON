print("****GOODIES STORE****")
sum=0
while(True):
    userInput=input("Enter the item price (or) press x to quit:\n")
    if(userInput!='x'):
        sum=sum+int(userInput)
        print(f"Order total so far: {sum}")
    else:
        print(f"Your bill total is {sum} . Thanks for shopping with our store")
        break

'''****GOODIES STORE****
Enter the item price (or) press x to quit:
56
Order total so far: 56
Enter the item price (or) press x to quit:
45
Order total so far: 101
Enter the item price (or) press x to quit:
89
Order total so far: 190
Enter the item price (or) press x to quit:
100
Order total so far: 290
Enter the item price (or) press x to quit:
200
Order total so far: 490
Enter the item price (or) press x to quit:
56
Order total so far: 546
Enter the item price (or) press x to quit:
89
Order total so far: 635
Enter the item price (or) press x to quit:
5600
Order total so far: 6235
Enter the item price (or) press x to quit:
x
Your bill total is 6235 . Thanks for shopping with our store
'''