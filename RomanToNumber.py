

ROMAN_NUMERALS = {'I': 1.0, 'V': 5.0, 'X': 10.0, 'L': 50.0, 'C': 100.0, 'D': 500.0, 'M': 1000.0}


def check_valid_roman(roman_list):
    for numeral in roman_list:
        if numeral.upper() not in ROMAN_NUMERALS:
            raise ValueError('Invalid Input')


def r_converter(numeral_list) -> list[float]:
    """Converts given numeral to its corresponding float value
    >>> r_converter('I')
    1
    >>> r_converter('X')
    10"""
    # for i in range(len(numeral_list)):
    #     numeral_list[i] = ROMAN_NUMERALS[numeral_list[i].upper()]
    numeral_list = [ROMAN_NUMERALS[numeral_list[i].upper()] for i in range(len(numeral_list))]
    return numeral_list


def roman_calculator(roman_list) -> float:
    """Returns a float that represents the Roman numerals provided.
    >>> roman_calculator(['X','C','I','V'])
    94
    >>> roman_calculator(['I','I','I'])
    3"""
    numbers = []
    i = 0
    try:
        check_valid_roman(roman_list)
        numbers = r_converter(roman_list)
        while i < len(numbers) - 1:
            if numbers[i] < numbers[i+1]:
                numbers[i] = numbers[i+1] - numbers[i]
                del numbers[i+1]
                i += 1
            else:
                i += 1
    except ValueError:
        print('Invalid Input')
        return -1
    return sum(numbers)


if __name__ == '__main__':
    print(roman_calculator(['X', 'B', 'I', 'V']))