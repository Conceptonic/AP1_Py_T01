def parse_float(s):
    s = s.strip()
    if not s:
        raise ValueError

    i = 0
    sign = 1
    if s[i] in ('+', '-'):
        if s[i] == '-':
            sign = -1
        i += 1

    if i == len(s):
        raise ValueError

    integer_part = 0
    decimal_part = 0
    decimal_places = 0
    has_digit = False

    while i < len(s) and s[i].isdigit():
        integer_part = integer_part * 10 + ord(s[i]) - ord('0')
        has_digit = True
        i += 1

    if i < len(s) and s[i] == '.':
        i += 1
        while i < len(s) and s[i].isdigit():
            decimal_part = decimal_part * 10 + ord(s[i]) - ord('0')
            decimal_places += 1
            has_digit = True
            i += 1

    if not has_digit:
        raise ValueError

    mantissa = sign * (integer_part + decimal_part / (10 ** decimal_places if decimal_places else 1))

    # Обработка научной нотации: e/E
    if i < len(s) and s[i] in ('e', 'E'):
        i += 1
        if i == len(s):
            raise ValueError
        exp_sign = 1
        if s[i] in ('+', '-'):
            if s[i] == '-':
                exp_sign = -1
            i += 1
        if i == len(s) or not s[i].isdigit():
            raise ValueError
        exp_value = 0
        while i < len(s) and s[i].isdigit():
            exp_value = exp_value * 10 + ord(s[i]) - ord('0')
            i += 1
        mantissa *= 10 ** (exp_sign * exp_value)

    if i != len(s):
        raise ValueError

    return mantissa


try:
    value = parse_float(input())
    print(f"{value * 2:.3f}")
except ValueError:
    print("Invalid input")