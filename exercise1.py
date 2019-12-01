from math import floor


def calculate_fuel(mass):
    return floor(mass/3) - 2

# Part 2: Loop until fuel required is less than zero.
def total_fuel_per_module(mass):
    fuel = mass
    total = 0
    while fuel >= 0:
        fuel = calculate_fuel(fuel)
        if fuel > 0:
            total += fuel
    return total

# Read the input mass file
data = open('exercise1/input.txt')

# Initialise variable to store total fuel requirement
total_fuel = 0

# Iterate through each entry in the input file, calculate fuel required and sum up the total
for value in data:
   total_fuel += total_fuel_per_module(int(value))

# Output the result
print(total_fuel)