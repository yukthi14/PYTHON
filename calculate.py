class calculate:
    def __init__(self,number):
        self.number=number
    def square(self):
        print(f"The value of {self.number} square is {self.number **2}")
    def squareRoot(self):
        print(f'The value of {self.number} squareRoot is {self.number **0.5}')
    def cube(self):
        print(f'the value of {self.number} cube is {self.number **3}')
    def cubeRoot(self):
        print(f'The value of {self.number} cubeRoot is {self.number **0.3}')
    @staticmethod
    def greet():
        print("***This program do some of the calculation***")
a=calculate(4)
a.square()
a.squareRoot()
a.cube()
a.cubeRoot()