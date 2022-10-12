leave_letter='''  NAME:<|NAME|>
Dear sir/madam 
I was not able to attend college due to common cold and fever.
my kindly request you to permit my leave application.
Thank you
USN:<|USN|>
BRANCH:<|BRANCH|>

Date:<|DATE|>
'''
name=input("Enter your name\n")
usn=input("Enter your usn\n")
branch=input("Enter your branch\n")
date=input("Enter date\n")
leave_letter=leave_letter.replace("<|NAME|>",name)
leave_letter=leave_letter.replace("<|USN|>",usn)
leave_letter=leave_letter.replace("<|BRANCH|>",branch)
leave_letter=leave_letter.replace("<|DATE|>",date)
print(leave_letter)

'''  Enter your name
yukthi
Enter your usn
1AM20IS112
Enter your branch
ISE
Enter date
12/10/2022


  NAME:yukthi
Dear sir/madam
I was not able to attend college due to common cold and fever.
my kindly request you to permit my leave application.
Thank you
USN:1AM20IS112
BRANCH:ISE

Date:12/10/2022
'''