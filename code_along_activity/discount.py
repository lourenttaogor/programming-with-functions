from datetime import datetime

discount_rate = .1
tax_rate = .06
today = datetime.now()
dow = today.weekday()
subtotal = 0
quantity = 1
while quantity != 0:
    quantity = int(input("what is the quantity of your order: "))
    if quantity != 0:
        price = float(input("what is the price: "))
        subtotal = quantity * price

print(f"Total order amount: {subtotal:.2f}")
discount = 0
if dow==2 or dow==3:
    if subtotal >= 50:
        discount = round(subtotal * discount_rate)
        print(f"Discount: {discount}")
    else:
        short = 50 - subtotal
        print(f"you can't get a discount order more items for ${short}")
subtotal -= discount
tax = round(subtotal * tax_rate)
total = subtotal + tax
print(f"Tax: {tax}")
print(f"Total: {total:.2f}")


