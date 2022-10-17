name=input("Enter your name:")
marks=input("Enter your marks:")
phone_number=input("Enter your phone number:")
usn=input("Enter your usn:")

template="The name of the student is {}, his marks are {} , phone number is {}, and usn is {}"
output=template.format(name,marks,phone_number,usn)
print(output)