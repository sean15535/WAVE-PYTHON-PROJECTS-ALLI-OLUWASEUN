# functional programming, obect oriented and procedural
#methods and attributes
class Car:
    def __init__(self, name, model,year, color):
        self.name= name
        self.model= model
        self.year=year
        self.color=color
    def drive(self):
        return "Zoom"

ride=Car("Toyota", "Camry", 2021 , 'red')
print(ride.drive())