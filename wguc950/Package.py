# Create class for packages
class Package:
    def __init__(self, ID, address, city, state, zipcode, Late_time, weight, status):
        # Unique identifier for the package.
        self.ID = ID
        # Delivery address of the package.
        self.address = address
        # City of the delivery address.
        self.city = city
        # State of the delivery address.
        self.state = state
        # Zipcode of the delivery address.
        self.zipcode = zipcode
        # Delivery time window for the package.
        self.Late_time = Late_time
        # Weight of the package.
        self.weight = weight
        # Current status of the package (Hub Center, In route, Delivered).
        self.status = status
        # Departure time from the hub.
        self.departure_time = None
        # Actual delivery time.
        self.delivery_time = None

    def __str__(self):
        # String representation of the Package object for easy inspection.
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zipcode,
                                                       self.Late_time, self.weight, self.delivery_time,
                                                       self.status)

    def update_status(self, convert_timedelta):
        # Update the status of the package based on the provided time.
        if self.delivery_time < convert_timedelta:
            self.status = "Delivered"
        elif self.departure_time > convert_timedelta:
            self.status = "In route"
        else:
            self.status = "Hub Center"
