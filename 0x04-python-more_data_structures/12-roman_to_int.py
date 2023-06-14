#!/usr/bin/python3
def roman_to_int(roman_string):
    intval = 0
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman_string) - 1):
        if roman_dict[roman_string[i]] >= roman_dict[roman_string[i + 1]]:
            intval += roman_dict[roman_string[i]]
        else:
            intval -= roman_dict[roman_string[i]]
    return intval + roman_dict[roman_string[-1]]
