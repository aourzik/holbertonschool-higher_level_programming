#!/usr/bin/python3

roman = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

def roman_to_int(roman_string):
    total = 0

    for i in range(len(roman_string)):
        current_roman = roman[roman_string[i]]

        if i + 1 < len(roman_string):
            next_roman = roman[roman_string[i + 1]]

            if current_roman < next_roman:
                total - current_roman
            else:
                total += current_roman
        else:
            total += current_roman
    return total
