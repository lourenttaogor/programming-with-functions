"""
This program calculates the fuel efficiency of a vehicle based on the distance traveled and the amount of fuel consumed.
It prompts the user to enter the distance traveled in miles and the amount of fuel consumed in gallons, then calculates and displays the fuel efficiency in miles per gallon (MPG).
"""

def main():
    # Get an odometer value in U.S. miles from the user.
    # Get another odometer value in U.S. miles from the user.
    # Get a fuel amount in U.S. gallons from the user.
    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    # Display the results for the user to see.

    start = float(input("Enter the starting odometer reading in miles: "))
    end = float(input("Enter the ending odometer reading in miles: "))
    gallons = float(input("Enter the amount of fuel consumed in gallons: "))

    mpg = miles_per_gallon(start, end, gallons)
    lp100k = lp100k_from_mpg(mpg)
    print(f"{mpg:.1f} miles per gallon")
    print(f"{lp100k:.2f} liters per 100 kilometers")
    pass

def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.
    Parameters
    start_miles: An odometer value in miles.
    end_miles: Another odometer value in miles.
    amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    mpg_numerator = end_miles - start_miles
    mpg_denominator = amount_gallons
    mpg = mpg_numerator / mpg_denominator

    return mpg

def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.
    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """

    lp100k_numerator = 235.215
    lp100k_denominator = mpg
    lp100k = lp100k_numerator / lp100k_denominator
    return lp100k

# Call the main function so that
# this program will start executing.
main()