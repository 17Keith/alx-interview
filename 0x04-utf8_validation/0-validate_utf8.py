#!/usr/bin/python3

""" UTF-8 Validation """


def validUTF8(data):
    """ A method that determines if a given data set \
        represents a valid UTF-8 encoding. """
    
    number_bytes = 0

    for i in data:
        if number_bytes == 0:
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                number_bytes = 1
            elif i >> 4 == 0b1110:
                number_bytes = 2
            elif i >> 3 == 0b11110:
                number_bytes = 3
            elif i >> 7 == 0b1:
                return False
        else:
            if i >> 6 != 0b10:
                return False
            number_bytes -= 1
    return number_bytes == 0
