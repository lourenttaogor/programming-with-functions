"""
Author: Okuku Ogorchukwu Lourentta
Purpose:I wrote a program that reads the CSV file and prints to the terminal window a receipt that lists the purchased items and shows the subtotal, the sales tax amount, and the total.
Exceeding the Requirements: Write code to print a reminder of how many days until the New Years Sale begins (Jan 1) at the bottom of the receipt.
"""

import csv
from datetime import datetime


# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()
def main():
    products_dict = read_dictionary('products.csv', 0)
    subtotal = 0.0
    total_items = 0
    print("Ambassador's Store")
    with open('request.csv', 'rt') as receipt_file:
        receipt_line = csv.reader(receipt_file)
        next(receipt_line)
        for line in receipt_line:
            product_number = line[0]
            if product_number in products_dict:
                product_info = products_dict[product_number]
                product_name = product_info[1]
                product_price = float(product_info[2])
                quantity = int(line[1])
                print(f"{product_name}:  {quantity} @ ${product_price:.2f}")
                total_items += quantity
                subtotal += product_price * quantity

    print(f"Total items purchased: {total_items}")
    print(f"Subtotal: ${subtotal:.2f}")
    sales_tax_rate = 0.06
    sales_tax = subtotal * sales_tax_rate
    print(f"Sales Tax: ${sales_tax:.2f}")
    total = subtotal + sales_tax
    print(f"Total: ${total:.2f}")
    print(f"{current_date_and_time:%A %I:%M %p}")
    #Write code to print a reminder of how many days until the New Years Sale begins (Jan 1) at the bottom of the receipt.
    new_years_sale_date = datetime(current_date_and_time.year + 1, 1, 1)
    days_until_new_years_sale = (new_years_sale_date - current_date_and_time).days
    print(f"Days until New Year's Sale: {days_until_new_years_sale} days")
    print("Thank you for shopping at Ambassador's Store!")



def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    dictionary = {}
    with open(filename, 'rt') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row

    return dictionary


if __name__ == "__main__":
    #Include a try block and except blocks to handle FileNotFoundError, PermissionError, and KeyError
    try:
        main()
    except FileNotFoundError:
        print(f"Error: File not found.")
    except PermissionError:
        print(f"Error: Please check your permissions to access the file.")
    except KeyError:
        print(f"Error. The product number does not exist in the product list.")
    except Exception:
        print(f"An unexpected error occurred")