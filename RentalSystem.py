import random

discount_code = random.randint(1000, 2000)

class Car():
    def __init__(self, availability, price_per_day):
        self.Available = availability
        self.price_per_day = price_per_day

Toyota = Car(True, 50)
Hyundai = Car(True, 40)
Nissan = Car(True, 45)


def system():
    while True:
        print("Welcome to the Car Rental System")
        print("Here is the list of cars:")

        if Toyota.Available:
            print("1. Toyota - $50 per day")
        else:
            print("1. Toyota - Not Available")

        if Hyundai.Available:
            print("2. Hyundai - $40 per day")
        else:
            print("2. Hyundai - Not Available")

        if Nissan.Available:
            print("3. Nissan - $45 per day")
        else:
            print("3. Nissan - Not Available")

        checkout = input("Select a car to rent (Toyota/Hyundai/Nissan): ")
        if checkout.lower() == "toyota" and Toyota.Available:
            def rent_toyota():
                days = input("How many days do you want to rent the Toyota? ")
    
                total_cost = int(days) * Toyota.price_per_day

                print(f"The total cost for renting the Toyota for {days} days is ${total_cost}.")
                print(f"Your discount code is: {discount_code}. Use this code to get a discount on your rental.")

                def normal_checkout():
                    while True:
                        normal_payment = input(f"Please insert {total_cost}.")
                        if int(normal_payment) >= total_cost: 
                            print("Payment successful. Thank you for renting with us!")
                            print("Returning change.")
                            Toyota.Available = False
                            break
                        else:
                            print("Inssuficient funds, Please try again.")

            
                def apply_discount():
                    discount_input = input(f"Input your discount code to apply a discount: ")
                    if discount_input == str(discount_code):
                        while True:
                            discounted_cost = total_cost * 0.9  # 10% discount

                            print(f"Discount applied! Your new total cost is: ${discounted_cost}.")
                            paying = input("Please pay here:")
                            if paying >= str(discounted_cost):
                                print("Payment successful. Thank you for renting with us!")
                                print("Returning change")
                                Toyota.Available = False
                                break
                            
                            else:
                                print("Payment failed. Please try again.")

                    else:
                        retry = input("Invalid discount code. No discount applied, try again? (y/n): ")
                        if retry.lower() == "y":
                            apply_discount()
                        else:
                            normal_checkout()
                while True:
                    option = input("Do you want to use a discount? (y/n)")
                    if option.lower() == "y":
                        apply_discount()
                        break
                    elif option.lower() == "n":
                        normal_checkout()
                        break
                    else:
                        print("Invalid option, Try again.")
            
            
            rent_toyota()


        if checkout.lower() == "hyundai" and Hyundai.Available:
            def rent_hyundai():
                days = input("How many days do you want to rent the Hyundai? ")
    
                total_cost = int(days) * Hyundai.price_per_day

                print(f"The total cost for renting the Hyundai for {days} days is ${total_cost}.")
                print(f"Your discount code is: {discount_code}. Use this code to get a discount on your rental.")

                def normal_checkout():
                    while True:
                        normal_payment = input(f"Please insert {total_cost}.")
                        if int(normal_payment) >= total_cost: 
                            print("Payment successful. Thank you for renting with us!")
                            print("Returning change.")
                            Hyundai.Available = False
                            break
                        else:
                            print("Inssuficient funds, Please try again.")

            
                def apply_discount():
                    discount_input = input(f"Input your discount code to apply a discount: ")
                    if discount_input == str(discount_code):
                        while True:
                            discounted_cost = total_cost * 0.9  # 10% discount

                            print(f"Discount applied! Your new total cost is: ${discounted_cost}.")
                            paying = input("Please pay here:")
                            if paying >= str(discounted_cost):
                                print("Payment successful. Thank you for renting with us!")
                                print("Returning change")
                                Nissan.Available = False
                                break
                            
                            else:
                                print("Payment failed. Please try again.")

                    else:
                        retry = input("Invalid discount code. No discount applied, try again? (y/n): ")
                        if retry.lower() == "y":
                            apply_discount()
                        else:
                            normal_checkout()
                while True:
                    option = input("Do you want to use a discount? (y/n)")
                    if option.lower() == "y":
                        apply_discount()
                        break
                    elif option.lower() == "n":
                        normal_checkout()
                        break
                    else:
                        print("Invalid option, Try again.")
            rent_hyundai()


        if checkout.lower() == "nissan" and Nissan.Available:
                     def rent_nissan():
                         days = input("How many days do you want to rent the Hyundai? ")
             
                         total_cost = int(days) * Nissan.price_per_day
         
                         print(f"The total cost for renting the Nissan for {days} days is ${total_cost}.")
                         print(f"Your discount code is: {discount_code}. Use this code to get a discount on your rental.")
         
                         def normal_checkout():
                             while True:
                                 normal_payment = input(f"Please insert {total_cost}.")
                                 if int(normal_payment) >= total_cost: 
                                     print("Payment successful. Thank you for renting with us!")
                                     print("Returning change.")
                                     Nissan.Available = False
                                     break
                                 else:
                                     print("Inssuficient funds, Please try again.")
         
                     
                         def apply_discount():
                             discount_input = input(f"Input your discount code to apply a discount: ")
                             if discount_input == str(discount_code):
                                 while True:
                                     discounted_cost = total_cost * 0.9  # 10% discount
         
                                     print(f"Discount applied! Your new total cost is: ${discounted_cost}.")
                                     paying = input("Please pay here:")
                                     if paying >= str(discounted_cost):
                                         print("Payment successful. Thank you for renting with us!")
                                         print("Returning change")
                                         Nissan.Available = False
                                         break
                                     
                                     else:
                                         print("Payment failed. Please try again.")
         
                             else:
                                 retry = input("Invalid discount code. No discount applied, try again? (y/n): ")
                                 if retry.lower() == "y":
                                     apply_discount()
                                 else:
                                     normal_checkout()
                         while True:
                             option = input("Do you want to use a discount? (y/n)")
                             if option.lower() == "y":
                                 apply_discount()
                                 break
                             elif option.lower() == "n":
                                 normal_checkout()
                                 break
                             else:
                                 print("Invalid option, Try again.")
                     rent_nissan()   

        else:
            print("Invalid selection or car not available.")
while True:
    start = input("Do you want to rent a car? (y/n): ")
    if start.lower() == "y":
        system()

    elif start.lower() == "n":
        returning = input("Are you here to return a car?")
        if returning.lower() == "y":
            print("yes")
        elif returning.lower() == "n":
            system()

        else:
            print("Invalid option, try again.")
            continue
    else:
        print("Invalid option, try again.")    
        continue