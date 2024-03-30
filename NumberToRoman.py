

ROMAN_NUMERALS = {'I': 1.0, 'V': 5.0, 'X': 10.0, 'L': 50.0, 'C': 100.0, 'D': 500.0, 'M': 1000.0}


def numeral_list(number):
    """Returns a list of roman numerals from a given number
    >>> numeral_list(22)
    ['X','X','I','I']"""
    roman_numerals = []
    while number > 0:
        if number / 1000.0 >= 1.0:
            roman_numerals.append('M')
            number -= 1000
        elif number / 900.0 >= 1:
            roman_numerals.append('C')
            roman_numerals.append('M')
            number -= 900
        elif number / 500.0 >= 1.0:
            roman_numerals.append('D')
            number -= 500.0
        elif number / 400.0 >= 1:
            roman_numerals.append('C')
            roman_numerals.append('D')
            number -= 400.0
        elif number / 100.0 >= 1.0:
            roman_numerals.append('C')
            number -= 100.0
        elif number / 90.0 >= 1:
            roman_numerals.append('X')
            roman_numerals.append('C')
            number -= 90.0
        elif number / 50.0 >= 1.0:
            roman_numerals.append('L')
            number -= 50.0
        elif number / 40.0 >= 1:
            roman_numerals.append('X')
            roman_numerals.append('L')
            number -= 40.0
        elif number / 10.0 >= 1.0:
            roman_numerals.append('X')
            number -= 10.0
        elif number / 9.0 >= 1:
            roman_numerals.append('I')
            roman_numerals.append('X')
            number -= 9.0
        elif number / 5.0 >= 1.0:
            roman_numerals.append('V')
            number -= 5.0
        elif number / 4.0 >= 1:
            roman_numerals.append('I')
            roman_numerals.append('V')
            number -= 4.0
        else:
            roman_numerals.append('I')
            number -= 1.0
    return roman_numerals

def number_to_roman(number):
    """Converts a number into a roman numeral
    >>> number_to_roman(94)
    XCIV
    >>> number_to_roman(18)
    XVIII
    """
    try:
        number = float(number)
    except:
        raise ValueError("Please enter a number")

    result_list = numeral_list(number)
    result_numeral = ''.join(result_list)

    return result_numeral




def number_parser(number, number_list=[])-> list[float]:
    """Returns a number broken up corresponding to its digit place.
    >>> number_parser(111)
    [1.0,10.0,100.0]
    >>> number_parser(9475)
    [5.0,70.0,400.0,9000.0]"""
    if number < 1:
        return number_list
    number_list += [float(number % 10)]
    return number_parser(number//10, number_list)


if __name__ == '__main__':
    print(number_to_roman(144))