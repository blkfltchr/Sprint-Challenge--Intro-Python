# To the GroundVehicle class, add method drive() that prints "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels

    # TODO

    def drive(self):
        print("vroooom") # print() returns an extra line of None


# Subclass Motorcycle from Vehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it prints "BRAAAP!!"

# TODO

class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels=2):
        super().__init__(num_wheels)
    def drive(self):
        return "BRAAAP!!" # return clears the extra None lines

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and call drive() on each.

# TODO

for vehicle in vehicles:
    print(vehicle.drive())
