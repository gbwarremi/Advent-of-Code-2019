
data = open('input.txt').read()
intcode_initial = [int(i) for i in data.split(',')]

# PART 1:

# Function to run the intcode calculation
def run_calculation(intcode_run):
    for instruction_pointer in range(0, len(intcode_run), 4):  # Step through intcode in intervals of 4 to access the instruction pointer
        if intcode_run[instruction_pointer] != 99:
            input_1, input_2, output_position = intcode_run[instruction_pointer + 1], intcode_run[instruction_pointer + 2], intcode_run[instruction_pointer + 3]
            # If instruction pointer is 1 then perform addition of place +1 and place +2 and store result in the position of the value held in place +3
            if intcode_run[instruction_pointer] == 1:
                intcode_run[output_position] = intcode_run[input_1] + intcode_run[input_2]
            # If instruction pointer is 2 then perform multiplication of place +1 and place +2 and store result in the position of the value held in place +3
            elif intcode_run[instruction_pointer] == 2:
                intcode_run[output_position] = intcode_run[input_1] * intcode_run[input_2]
        else:
            break
    return intcode_run[0]   # Return the result of position 0

intcode_input = intcode_initial.copy()  # Create of copy of the initial intcode to run in the calculation for part 1
intcode_input[1], intcode_input[2] = 12, 2  # Set the positions 1 & 2 as per the instructions for part 1
print(f'Part 1: Result = {run_calculation(intcode_input)}') # Perform the calculation for part 1 and output the result


# PART 2:

def gravity_assist(expected_result):
    result = 0  # initialise variable to store results
    for noun in range(100): # Loop through noun from 0 to 99
        for verb in range(100): # Loop through verb from 0 to 99
            intcode_input = intcode_initial.copy()  # initialise the input intcode
            intcode_input[1], intcode_input[2] = noun, verb # Set the positions 1 & 2 to the values of noun and verb
            result = run_calculation(intcode_input) # Run the intcode calculation based on the noun and verb values and store the result
            if result == expected_result:   # If the result matches the expected result then break out of loop and return results
                return result, noun, verb

result, noun, verb = gravity_assist(19690720)   # Run gravity assist function with value to be found
print(f'Part 2: Result = {result}, Verb = {verb}, Noun = {noun}, Entry (100 * noun + verb) = {100 * noun + verb}')