import string
import random

if __name__ == "__main__":
    s1=string.ascii_lowercase
    #print(s1)
    #abcdefghijklmnopqrstuvwxyz
    s2=string.ascii_uppercase
    #print(s2)
    #ABCDEFGHIJKLMNOPQRSTUVWXYZ
    s3=string.digits
    #print(s3)
    #0123456789
    s4=string.punctuation
    #print(s4)
    #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    plen=int(input('Enter password length\n'))
    s=[]
    s.extend(list(s1))   #converts s1 to list
    s.extend(list(s2))   #converts s2 to list
    s.extend(list(s3))   #converts s3 to list
    s.extend(list(s4))   #converts s4 to list
    #print(s)
    #random.shuffle(s)   #method-1
    #print(s)
    print("Your password is :")
    print("".join(random.sample(s,plen)))   #method-2
    #print("".join(s[0:plen]))

'''Enter password length
8
Your password is :
O+tP|'um
'''