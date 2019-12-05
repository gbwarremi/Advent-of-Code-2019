
def is_Valid_Code(code):
    two_occurrences = False   # Flag to log 2 occurrences of number in code
    previous = 0   # Store the previous number in the code to check current number against
    valid = True    # Initialise variable to determine if code is valid (default as valid)

    for digit in code:   # Loop through the code
        if int(digit) < previous:    # If current number is less than previous number if code then return False
            return False
        elif code.count(digit) == 2:    # Check if number if code has 2 occurrences and update flag if found
            two_occurrences = True
        previous = int(digit)

    if not two_occurrences:    # If 2 occurrences of a number were not found in the code then set code to false
        valid = False

    return valid


start, end = 108457, 562041

valid_codes = [i for i in range(start, end+1) if is_Valid_Code(str(i))]
print(f'The number of codes with matching pattern is: {len(valid_codes)}')