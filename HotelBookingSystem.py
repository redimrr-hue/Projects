import random

class rooms:
    def __init__(self, name, vacancy, type, price, pin):
        self.name = name
        self.vacancy = vacancy
        self.type = type
        self.price = price
        self.pin = pin

#All the rooms
Room_10 = rooms("Room 10",random.choice([True, False]), "VIP", 150, random.randint(1000, 9999))
Room_9 = rooms("Room 9",random.choice([True, False]), "VIP", 150, random.randint(1000, 9999))
Room_8 = rooms("Room 8",random.choice([True, False]), "VIP", 150, random.randint(1000, 9999))
Room_7 = rooms("Room 7",random.choice([True, False]), "VIP", 150, random.randint(1000, 9999))
Room_6 = rooms("Room 6",random.choice([True, False]), "VIP", 150, random.randint(1000, 9999))
Room_5 = rooms("Room 5",random.choice([True, False]), "Standard", 50, random.randint(1000, 9999))
Room_4 = rooms("Room 4",random.choice([True, False]), "Standard", 50, random.randint(1000, 9999))
Room_3 = rooms("Room 3",random.choice([True, False]), "Standard", 50, random.randint(1000, 9999))
Room_2 = rooms("Room 2",random.choice([True, False]), "Standard", 50, random.randint(1000, 9999))
Room_1 = rooms("Room 1",random.choice([True, False]), "Standard", 50, random.randint(1000, 9999))

all_rooms = [
    Room_10, Room_9, Room_8, Room_7, Room_6,
    Room_5, Room_4, Room_3, Room_2, Room_1
]

print("Welcome to FBT Hotel!")


def openrooms():
    print("Here are all the available rooms:")
    #Printing only the available rooms
    for room in all_rooms:
        if room.vacancy == True:
            print(room.name, room.type)

def reciept(room, nights, finalprice, payment):
    change = int(payment) - int(finalprice)

    print("\n===================================")
    print("          FBT HOTEL")
    print("          BOOKING RECEIPT")
    print("===================================")
    print("-----------------------------------")
    print(f"Room:          {room.name}")
    print(f"Room type:     {room.type}")
    print(f"Price per night: {room.price} SAR")
    print(f"Number of nights: {nights}")
    print("-----------------------------------")
    print(f"Total cost:    {finalprice} SAR")
    print(f"Payment:       {payment} SAR")
    print(f"Change:        {change} SAR")
    print("===================================")
    print("     Thank you for staying!")
    print("===================================\n")

def booking():
    while True:
        roomchoice = input("Please choose a room (enter return to return.): ")
        if roomchoice.lower() == "return":
                   return
        for room in all_rooms:
            if room.name.lower() == roomchoice.lower():

                if room.vacancy:
                    print(f"You have chosen {room.name}, ({room.type}), which will cost you {room.price} SAR per night.")
                    nights = input("How many nights do you plan on staying?: ")
                    finalprice = room.price * int(nights)
                    print(f"That will be {finalprice} SAR")
                    while True:
                        payment = input("Please pay here: ")
                        if int(payment) >= finalprice:
                            print("Thank you, change will be given shortly")
                            print(f"Please remember, this is you pin: {room.pin}")
                            room.vacancy = False
                            reciept(room, nights, finalprice, payment)
                            return
                        else:
                            print("Insufficient funds, Please try again.")
                
                else:
                    print(f"Sorry, {room.name} is occupied.")
                    break
    
        else:
            print("Room not found. Please choose a valid room.")
            return

def checkingout():
    while True:
        currentroom = input("Please enter your room number (enter return to return.): ")
        if currentroom.lower() == "return":
           return
        for room in all_rooms:
            if room.name.lower() == currentroom.lower():

                if not room.vacancy:
                    confirm = input("Please enter the pin: ")
                    if confirm == str(room.pin):
                        print("Succesfully checked out, Thank you for staying")
                        room.vacancy = True
                        room.pin = random.randint(1000,9999)
                        return
                else:
                    print("Pin is incorrect.")

        else:
            print("Invalid room name. Please try again.")


while True:
    type = input("Are you booking? Or checking out?: ")
    if type.lower() == "booking":
        openrooms()
        booking()
    elif type.lower() == "checking out":
        checkingout()
    else:
        print("Invalid choice.")