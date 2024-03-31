ROMAN_NUMERALS = {'M': 1000.0, 'CM': 900.0, 'D': 500, 'CD': 400.0, 'C': 100, 'XC': 90.0, 'L': 50.0, 'XL': 40.0,
                  'X': 10.0, 'IX': 9.0, 'V': 5.0, 'IV': 4.0, 'I': 1.0}


def numeral_list_2(number):
    """Returns a list of roman numerals from a given number
    >>> numeral_list_2(22)
    ['X','X','I','I']"""
    roman_numerals = []
    while number > 0:
        for elem in ROMAN_NUMERALS:
            if number / ROMAN_NUMERALS[elem] >= 1:
                roman_numerals.append(elem)
                number -= ROMAN_NUMERALS[elem]
                break
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
    except ValueError:
        return -1
    if number >= 4000:
        return -2
    if number < 1:
        return -3
    result_list = numeral_list_2(number)
    result_numeral = ''.join(result_list)

    return result_numeral