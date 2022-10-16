try:
    a=int(input("Enter a number :"))
    c=1/a
    print(c)
except ValueError as e:
    print("Enter a number:")
    print(e)
except ZeroDivisionError as e:
    print("Make sure you are not dividing by 0 ")
print("Thanks for using code !")