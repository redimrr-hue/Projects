import random
def reciept():
    print("----- Parking Receipt -----")
    print(f"Payment: ${payment}")
    print("Thank you for using our parking lot!")
    print("---------------------------")

intro = input("Welcome to the parking lot! Are you entering the parking lot? (y/n): ")
if intro.lower() == 'y':
    available_spaces = random.randint(0, 5)
    print(f"Available parking spaces: {available_spaces}")

    if available_spaces > 0:
        print("You can park your vehicle. the fee is $5 per hour.")
        plate_number = input("Please enter your plate number: ")
        print(f"Your plate number is {plate_number}.")
    else:
        print("Sorry, the parking lot is full.")

elif intro.lower() == 'n':
    leaving_intro = input("Are you leaving the parking lot? (y/n): ")
    if leaving_intro.lower() == 'y':
        plate_number_ex = input("Please enter your plate number to leave the parking lot: ")
        cost = random.randint(1, 5)
        total = cost * 5
        running = True
        while running:
            print(f"You have spent{cost} hours in the parking lot. the fee is ${cost * 5}")
            payment = float(input("Please enter your payment amount: $"))
            if payment < total:
                print("Insufficient payment. Please insert more money.")
                continue
            else:
                reciept()
                running = False
                break
else:
    print("Thank you for visiting the parking lot. Have a great day!")