class Train:
    def __init__(self,name,fare,seats,time):
        self.name=name
        self.fare=fare
        self.seats=seats
        self.time=time
    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
    def fareInfo(self):
        print(f"The price of the ticket is : Rs {self.fare} ")
    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked!! Your seat number is {self.seats}")
            self.seats=self.seats - 1
        else:
            print("Sorry this train is full")
    def departureTime(self):
        print(f"The train would depart at = {self.time}")
    

Fast_Express=Train("Fast express : 1409", 4000, 4, '22:30 pm' ) 
Fast_Express.getStatus()
Fast_Express.fareInfo()
Fast_Express.departureTime()
Fast_Express.bookTicket()
Fast_Express.getStatus()