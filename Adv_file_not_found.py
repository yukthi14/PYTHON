def readfile(filename):
    try:
        with open(filename,'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} is not found")
        
readfile("1.txt")
readfile("2.txt")
readfile("3.txt")