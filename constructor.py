class programmer:
    company ='Accenture'
    def __init__(self, name, product) :
       self.name=name
       self.product=product
       
    def getInfo(self):
        print(f"The name of the company {self.company} and programmer {self.name} and the product {self.product}")
    
    
yukthi=programmer("yukthi","AWS")
sneha=programmer('sneha','IOT')
srija=programmer('srija','cloud computing')
yukthi.getInfo()
sneha.getInfo()
srija.getInfo()
    

