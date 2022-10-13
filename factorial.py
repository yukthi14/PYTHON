number=int(input("Enter the number:\n"))
factorial=1
for i in range(1,number+1):
    factorial=factorial*i
print(f"The factorial of {number} is:\n{factorial}")

'''f=4
for i in range(n):
    f=f*(i+1)
    print(f)
'''
''' def fact(n):
      if n==0 or n==1:
        return 1
    return n*fact(n-1)
    f=fact(4)
    print(f)
'''