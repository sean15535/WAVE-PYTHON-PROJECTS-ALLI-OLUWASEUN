# functional programming, obect oriented and procedural
#methods and attributes
# class Car:
#     def __init__(self, name, model,year, color):
#         self.name= name
#         self.model= model
#         self.year=year
#         self.color=color
#     def drive(self):
#         return "Zoom"

# ride=Car("Toyota", "Camry", 2021 , 'red')
# print(ride.drive())

class Wifi:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def connect(self):
        if self.name == username and self.password == password:
            return "Connected"
        else:
            return "Invalid Username or Pass"

wifi_name = str(input("Enter Wifi Username: "))
wifi_password = str(input("Enter Wifi Password: "))

my_wifi = Wifi(wifi_name, wifi_password)
result = my_wifi.connect(self, username, password)
print(result)




