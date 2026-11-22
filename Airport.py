class Passenger:
    def __init__(self, passengerID, name, passportNumber, nationality):
        self.passengerID = passengerID
        self.name = name
        self.passportNumber = passportNumber
        self.nationality = nationality

class Boardingpass:
    def __init__

def bookticket():
    passengerID = input("Enter Passenger ID: ")
    name = input("Enter Name: ")
    passportNumber = input("Enter Passport Number: ")
    nationality = input("Enter Nationality: ")

    passenger = Passenger(passengerID, name, passportNumber, nationality)
    print("Ticket booked successfully for", passenger.name)

