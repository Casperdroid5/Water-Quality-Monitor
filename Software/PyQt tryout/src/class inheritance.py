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