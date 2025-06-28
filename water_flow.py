"""
Author: Okuku Lourentta
Purpose:Prove that you can write a Python program and write and run test functions to
help you find and fix mistakes in your program. Write the second half of the Python program to help an engineer design a water distribution system. Also, write more test functions that will automatically verify that your program functions work correctly.
Exceeded requirements by saving 9.8066500, 998.2, and 0.0010016 to variables, and subtituting the values in the functions
with the variable names. I also defined a function that converts kilopascals to pounds per square inch and called the function at the bottom
of the code to give the pressure value in psi. i also test my converter function in the test_water_flow file

"""
EARTH_ACCELERATION_OF_GRAVITY = 9.8066500
WATER_DENSITY = 998.2000000
WATER_DYNAMIC_VISCOSITY = 0.0010016

def water_column_height(tower_height, tank_height):
    """
    water_column_height that calculates and returns the height of a column of water from a tower height and a tank wall height

    using the formula:
    height_water_column = height_tower + (3 (tank_height) / 4)
4
    """

    # calculate the tank height using the formula
    bodmas = 3 * tank_height / 4
    # Calculate the height of the water column using the formula
    height_water_column = tower_height + bodmas

    # Return the calculated height of the water column
    return height_water_column

def pressure_gain_from_water_height(height):
    """
    calculates and returns the pressure caused by Earth's gravity pulling on the water stored in an elevated tank
    """

    pressure = (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000

    return pressure


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """
    calculates and returns the water pressure lost because of the friction between the water and the walls of a pipe that it flows through.
    """

    pressure_loss = (-friction_factor * pipe_length * WATER_DENSITY * (fluid_velocity ** 2)) / (2000 * pipe_diameter)

    return pressure_loss


def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """
    calculates the water pressure lost because of fittings such as 45° and 90° bends that are in a pipeline
    """
    loss_pressure = (-0.04 * WATER_DENSITY * (fluid_velocity ** 2) * quantity_fittings) / 2000
    return loss_pressure

def reynolds_number(hydraulic_diameter, fluid_velocity):

    """
    calculates and returns the Reynolds number for a pipe with water flowing through it
    """

    reynolds = WATER_DENSITY * hydraulic_diameter * fluid_velocity / WATER_DYNAMIC_VISCOSITY 

    return reynolds

def pressure_loss_from_pipe_reduction(larger_diameter,fluid_velocity, reynolds_number, smaller_diameter):
    """
    calculates the water pressure lost because of water moving from a pipe with a large diameter into a pipe with a smaller diameter
    """

    K = (0.1 + (50 / reynolds_number)) * ((larger_diameter / smaller_diameter) ** 4 -1)
    pressure_loss = -K * WATER_DENSITY * (fluid_velocity ** 2) / 2000

    return pressure_loss

def converter(kpa):
    #converts kilopascals to pounds per square

    return kpa * 0.145038



PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    convert = converter(pressure)
    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {convert:.1f} per square inch ")
if __name__ == "__main__":
    main()