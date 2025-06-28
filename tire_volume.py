"""
Author: Okuku Ogorchukwu Lourentta
Project: Tire Volume Calculation

Purpose: To compute the approximate volume of air inside a tire.

Showed creativity by acking the user if he/she wants to buy a tire with the dimentions entered.
"""
from datetime import datetime
import math

# Constants
pi = math.pi
width = int(input("Enter the tire width in mm: "))
aspect_ratio = int(input("Enter the tire aspect ratio: "))
diameter = int(input("Enter the tire diameter in inches: "))

#calculating the volume of air inside the tire
v_numerator = pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)
v_denominator = 10000000000
tire_volume = v_numerator / v_denominator
print(f"The approximate volume of air inside the tire is: {tire_volume:.2f} liters")

today = datetime.now()
formatted_date = f"{today:%Y-%m-%d}"
phone_number = " "

#open vo;umes.txt in append mode
with open("volumes.txt", "at") as volumes_file:
    print(f" {formatted_date}, {width}, {aspect_ratio}, {diameter}, {tire_volume:.2f}", file=volumes_file)


#Exceeding the requirements
tire_price = tire_volume * 10  # Assuming a price of $10 per liter of air
purchase_enquiry = input("Do you want to buy a tire with these dimensions? (yes/no): ").strip().lower()
if purchase_enquiry == "yes":
    quantity = int(input("How many tires do you want to buy?"))
    phone_number = input("Please enter your phone number: ")
    total_price = tire_price * quantity
    with open("volumes.txt", "at") as volumes_file:
        print(f" {formatted_date}, {width}, {aspect_ratio}, {diameter}, {tire_volume:.2f}, {phone_number}", file=volumes_file)
    print(f"The total price for {quantity} tires is: ${total_price:.2f}")
else:
    print("Thank you for your inquiry. Have a great day!")


