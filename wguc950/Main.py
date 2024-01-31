
from builtins import ValueError
from CreateHashTable import CreateHashTable
from Package import Package
import csv
import datetime
import Truck
# Packages are arranged on a truck based on the nearest neighbor algorithm
# this method also determines the distance a truck must go after the packages are sorted.
def packages_route(truck):

    # Sort all shipments into the "unfinished route".
    unfinished_route = list(truck.packages)
    # Empty the package list from a specific vehicle so that the products can be re-loaded in the neighbor's order.
    truck.packages.clear()

    # Cycle through the list of unfinished route until none remain in the list
    # Adds the nearest package into the truck.packages list one by one
    while unfinished_route:

        current_direction = extract_address_number(truck.address)
        next_package_id = nearest_address(current_direction, unfinished_route)

        if next_package_id is not None:

            next_package = package_hash_table.lookup(next_package_id)
            (h, m, s) = "10:20:00".split(":")
            if next_package.ID == 9 and truck.time >= datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s)):
                next_package.address = "410 S State St"
                next_package.zipcode = "84111"
            unfinished_route.remove(next_package_id)
            # Updates the time it took for the truck to drive to the nearest package
            next_address = get_current_distance(current_direction, extract_address_number(next_package.address))
            truck.mileage += next_address
            truck.time += datetime.timedelta(hours=next_address / 18)


            next_package.delivery_time = truck.time
            next_package.departure_time = truck.depart_time
            truck.address = next_package.address
        else:
            break

def nearest_address(current_address, not_delivered):
    nearest_package_id = None
    min_distance = float('inf')


    for package_id in not_delivered:
        package = package_hash_table.lookup(package_id)
        package_address = extract_address_number(package.address)
        distance = get_current_distance(current_address, package_address)

        if distance < min_distance:
            min_distance = distance
            nearest_package_id = package_id


    return nearest_package_id

# Loading up truck 1
set_up_truck1 = Truck.Truck([1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 0.0,
                            "4001 South 700 East", datetime.timedelta(hours=8), 16, 18, None)

# Loading up truck 2
set_up_truck2 = Truck.Truck([3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0,
                            "4001 South 700 East", datetime.timedelta(hours=10, minutes=20), 16, 18, None,)

# Loading up truck 3
set_up_truck3 = Truck.Truck([2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 0.0,
                            "4001 South 700 East", datetime.timedelta(hours=9, minutes=5), 16, 18, None,)

# Method for finding distance between two addresses
def get_current_distance(x, y):
    length = Distance_CSV[x][y]
    if length == '':
        length = Distance_CSV[y][x]

    return float(length)

# Read the file of distance information
with open("CSV/Distance_File.csv") as csvfile1:
    Distance_CSV = list(csv.reader(csvfile1))

# Read the file of address information
with open("CSV/Address_File.csv") as csvfile2:
    Address_CSV = list(csv.reader(csvfile2))

#From the CSV package file, create package objects. Place package objects into the package_hash_table hash table.
def load_data(filename, package_hash_table):
    with open(filename) as package_info:
        package_data = csv.reader(package_info)
        for package in package_data:
            package_ID = int(package[0])
            package_Address = package[1]
            package_City = package[2]
            package_State = package[3]
            package_Zipcode = package[4]
            Late_time = package[5]
            package_Weight = package[6]
            package_Status = "Hub Center"


            # Package Item
            pack = Package(package_ID, package_Address, package_City, package_State, package_Zipcode, Late_time, package_Weight, package_Status)

            # Add information to the hash table
            package_hash_table.insert(package_ID, pack)

# Method to get address number from string literal of address
def extract_address_number(address):
    for row in Address_CSV:
        if address in row[2]:
            return int(row[0])

# Create hash table
package_hash_table = CreateHashTable()

# Load packages into hash table
load_data("CSV/Package_File.csv", package_hash_table)

#Truck 3 doesn't depart until both of the preceding two trucks are completed.
packages_route(set_up_truck1)
packages_route(set_up_truck2)
set_up_truck3.depart_time = min(set_up_truck1.time, set_up_truck2.time)
packages_route(set_up_truck3)

def command_prompt(quit = False):
    if not quit:
        # User Interface
        # Upon running the program, the below message will appear.
        print("The mileage for the route is:")
        print(set_up_truck1.mileage + set_up_truck2.mileage + set_up_truck3.mileage)
        print('*********************** COMMANDS ***********************\n')
        print(' 1. All Packages\n')
        print(' 2. One Package\n')
        print('*********************** END COMMANDS ***********************\n')

        user_input = input('\nEnter command here (to see all commands type h):\n').lower()

        if user_input == 'q' or user_input == 'quit':
            exit('Thank you for using WGUPS!')
        if user_input == 'h' or user_input == 'help':
            command_prompt(False)

        if user_input == '1':
            try:
                # The user will be asked to enter a specific time
                user_time = input("Please enter a time (HH:MM:SS): ")
                (h, m, s) = user_time.split(":")
                convert_timedelta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

                for packageID in range(1, 41):
                    delivered_or_not = package_hash_table.lookup(packageID)
                    delivered_or_not.update_status(convert_timedelta)
                    print(str(delivered_or_not))
            except ValueError:
                print("Invalid Input. Closing program.")
                exit()

        elif user_input == '2':
            try:
                # The user will be asked to enter package ID
                one_package = input("Enter the numeric package ID: ")
                # The user will be asked to enter a specific time
                user_time = input("Please enter a time (HH:MM:SS): ")
                (h, m, s) = user_time.split(":")
                convert_timedelta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

                delivered_or_not = package_hash_table.lookup(int(one_package))
                delivered_or_not.update_status(convert_timedelta)
                print(str(delivered_or_not))
            except ValueError:
                print("Invalid Input. Closing program.")
                exit()
        command_prompt()


    else:
        print("Invalid Input. Closing program.")
        exit()

command_prompt()
