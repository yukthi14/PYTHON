


secure=(('y','@'),('k','K'),('i','&'),('1','^'),('0','o'),('9','#'))
def securePassword(password):
    for a,b in secure:
        password=password.replace(a,b)
    return password


if __name__ == "__main__":
    password=input("Enter your password:\n")
    password=securePassword(password)
    print(f"Your secure password is : {password} ")