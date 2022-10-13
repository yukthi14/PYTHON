a=input("Enter first subject name:\n")
sub1=int(input("Enter first subject marks\n"))
b=input("Enter second subject name:\n")
sub2=int(input("Enter second subject marks\n"))
c=input("Enter third subject name:\n")
sub3=int(input("Enter third subject marks\n"))
d=input("Enter fourth subject name:\n")
sub4=int(input("Enter fourth subject marks\n"))

if(sub1<40 or sub2<40 or sub3<40 or sub4<40):
    print("You are failed because scored marks is less then 40")
elif(sub1+sub2+sub3+sub4)/4<40:
    print("You are failed,total percentage less than 40")

else:
    print("Congatulations!!! You have passed the exam")


   

