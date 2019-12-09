
data = open('input_Day7.txt').read()
# data = '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5' # Max thruster signal 139629729 (from phase setting sequence 9,8,7,6,5)
# data = '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0' # Max Thrust = 54321 (from phase setting sequence 0,1,2,3,4)
# data = '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0' # Max Thrust = 65210 (from phase setting sequence 1,0,4,3,2)
int_code = [int(i) for i in data.split(',')]

class Amplifier:
    def __init__(self, int_code, phase):
        self.int_code = int_code
        self.inputs = []
        self.inputs.append(phase)
        self.steps = {'01': 4, '02': 4, '03': 2, '04': 2, '05': 3, '06': 3, '07': 4, '08': 4}
        self.index = 0
        self.input_index = 0
        self.isActive = True
        self.output = 0

    def run(self, result):
        self.inputs.append(result)
        while self.index < len(self.int_code) and self.isActive:
            instruction = str(self.int_code[self.index]).zfill(5)
            action = instruction[-2:]
            if action == '99':
                self.isActive = False
                return None

            try:
                mode1 = self.int_code[self.index + 1] if instruction[-3:-2] == '0' else self.index + 1
            except Exception as err:
                self.isActive = False
            try:
                mode2 = self.int_code[self.index + 2] if instruction[-4:-3] == '0' else self.index + 2
            except Exception as err:
                self.isActive = False
            try:
                mode3 = self.int_code[self.index + 3] if instruction[-5:-4] == '0' else self.index + 3
            except Exception as err:
                self.isActive = False


            # Opcode 01: Add parameters
            if action == '01':
                self.int_code[mode3] = self.int_code[mode1] + self.int_code[mode2]
            # Opcode 02: Multiply parameters
            elif action == '02':
                self.int_code[mode3] = self.int_code[mode1] * self.int_code[mode2]
            # Opcode 03 takes a single integer as input and saves it to the position given by its only parameter. For example, the instruction 3,50 would take an input value and store it at address 50.
            elif action == '03':
                try:
                    self.int_code[mode1] = self.inputs[self.input_index]
                    self.input_index += 1
                except Exception as err:
                    print(err)
                    print('No more inputs, return None')
                    return None
            # Opcode 04 outputs the value of its only parameter. For example, the instruction 4,50 would output the value at address 50.
            elif action == '04':
                self.output = self.int_code[mode1]
                self.index += 2
                return self.output            # self.int_code[mode1]
            # Opcode 05 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
            elif action == '05':
                if self.int_code[mode1] != 0:
                    self.index = self.int_code[mode2]
                    continue
            # Opcode 06 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
            elif action == '06':
                if self.int_code[mode1] == 0:
                    self.index = int_code[mode2]
                    continue
            # Opcode 07 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
            elif action == '07':
                if self.int_code[mode1] < self.int_code[mode2]:
                    self.int_code[mode3] = 1
                else:
                    self.int_code[mode3] = 0
            # Opcode 08 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
            elif action == '08':
                if self.int_code[mode1] == self.int_code[mode2]:
                    self.int_code[mode3] = 1
                else:
                    self.int_code[mode3] = 0

            self.index += self.steps.get(action)  # Increase pointer by number of steps stored in the dictionary
        return None


combinations = []
for i1 in range(5,10):
    for i2 in range(5,10):
        if i2 == i1:
            continue
        for i3 in range(5,10):
            if i3 == i2 or i3 == i1:
                continue
            for i4 in range(5,10):
                if i4 == i3 or i4 == i2 or i4 == i1:
                    continue
                for i5 in range(5,10):
                    if i5 == i4 or i5 == i3 or i5 == i2 or i5 == i1:
                        continue
                    combinations.append([i1, i2 , i3, i4, i5])

results = []
results_combinations = []
for combination in combinations:
    result = 0
    amps = []
    for phase in combination:
        amp = Amplifier(int_code.copy(), phase)
        amps.append(amp)
    i = 0
    while result != None:
        i += 1
        for amp in amps:
            result = amp.run(result)
    results.append(amps[4].output)
    results_combinations.append(combination)

print(max(results))
print(results_combinations[results.index(max(results))])


