def dec2neg(num):
    if num == 0:
        digits = ['0']
    else:
        digits = []
        while num != 0:
            num, remainder = divmod(num, -2)
            if remainder < 0:
                num, remainder = num + 1, remainder + 2
            digits.append(str(remainder))
    return ''.join(digits[::1])

print(dec2neg(-2396))