
data = open('input_Day5.txt').read()
int_code = [int(i) for i in data.split(',')]

# Use dictionary to store number of steps the pointer should move after processing an instruction
steps = {'01': 4, '02': 4, '03': 2, '04': 2, '05': 3, '06': 3, '07': 4, '08': 4}

i = 0
while i < len(int_code):

    instruction = str(int_code[i]).zfill(5)
    action = instruction[-2:]

    if action == '99':
        break

    mode1 = int_code[i+1] if instruction[-3:-2] == '0' else i+1
    mode2 = int_code[i+2] if instruction[-4:-3] == '0' else i+2
    mode3 = int_code[i+3] if instruction[-5:-4] == '0' else i+3

    # Collection of if statements used to carry out each instruction:
    if action == '01':
        int_code[mode3] = int_code[mode1] + int_code[mode2]
    elif action == '02':
        int_code[mode3] = int_code[mode1] * int_code[mode2]
    elif action == '03':
        entry = int(input('Please enter input: '))
        int_code[mode1] = entry
    elif action == '04':
        print(int_code[mode1])
    elif action == '05':
        if int_code[mode1] != 0:
            i = int_code[mode2]
            continue
    elif action == '06':
        if int_code[mode1] == 0:
            i = int_code[mode2]
            continue
    elif action == '07':
        if int_code[mode1] < int_code[mode2]:
            int_code[mode3] = 1
        else:
            int_code[mode3] = 0
    elif action == '08':
        if int_code[mode1] == int_code[mode2]:
            int_code[mode3] = 1
        else:
            int_code[mode3] = 0

    i += steps.get(action) # Increase pointer by number of steps stored in the dictionary


