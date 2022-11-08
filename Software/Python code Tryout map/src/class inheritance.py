class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

X = Vehicle("Harry", 60, 100)

print(X)
print(X.name)
print(X.max_speed)
print(X.mileage)
       
# print (type(name))
# class variables
class Vehicle:
    color = "white"
    
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

schoolbus = Bus("harry", 80, 10000)
racecar = Car("lightning", 180, 2300)

print(schoolbus.color, schoolbus.name, schoolbus.max_speed, schoolbus.mileage)
print(racecar.color, racecar.name)

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare (self):
       amount = super().fare()
       amount += (amount * 10)/100
       return amount
    

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())