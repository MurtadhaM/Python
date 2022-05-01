
class Fish():
    def    __init__(self):
        self.name = " "
        self.fish = dict.fromkeys((0,1,2,3,4,5,6,7,8))
        
        self.age = 0
        self.newBorns =   {}
        

    def print(self):
       print(self.name)
    def set_name(self,name):
        self.name = name
    def __str__(self):
         parameters = " "
         for parameter in self.__dict__:
             parameters += "parameter: " + str(parameter) + "\n"
         return parameters
     
    def process_fish(self, day):
        print(self.fish)
        


days = 2

myobj =   Fish()

    

for day in range(days):
    myobj.process_fish(day)
    
        


print(myobj.fish)


print(myobj)


