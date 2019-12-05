
def is_Valid_Code(code):
    consecutive_flag, valid = False, True
    previous = 0

    for digit in code:
        if int(digit) < previous:
            valid = False
            break
        elif int(digit) == previous:
            consecutive_flag = True
        previous = int(digit)
    if not consecutive_flag:
        valid = False
    return valid


start = 108457
end = 562041

valid_codes = [i for i in range(start, end+1) if is_Valid_Code(str(i))]
print(len(valid_codes))