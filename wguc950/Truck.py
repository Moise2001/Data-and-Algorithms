# Create class for trucks
class Truck:
    def __init__(self, packages, mileage, address, depart_time, capacity, speed, load):
        # List of package IDs loaded onto the truck.
        self.packages = packages
        # Total mileage covered by the truck during its route.
        self.mileage = mileage
        # Current address of the truck.
        self.address = address
        # Departure time of the truck from the hub.
        self.depart_time = depart_time
        # Current time of the truck during its route.
        self.time = depart_time
        # Maximum capacity (number of packages) the truck can carry.
        self.capacity = capacity
        # Speed of the truck.
        self.speed = speed
        # Load status of the truck.
        self.load = load

    def __str__(self):
        # String representation of the Truck object for easy inspection.
        return "%s, %s, %s, %s, %s, %s, %s" % (self.packages, self.mileage,
                                               self.address, self.depart_time, self.capacity, self.speed, self.load)
