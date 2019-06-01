# -*- coding: utf-8 -*-
"""
Created on Wed May 22 15:47:48 2019

@author: AG
"""

class CgiEnDecoder:
    def CgiDecode(encodedStr):
        """Decode the CGI-encoded string:
           * replace "+" by " "
           * replace "%xx" by the character with hex number xx.
           Return the decoded string.  Raise `ValueError` for invalid inputs."""
    
        # Mapping of hex digits to their integer values
        hex_values = {
            '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
            '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
            'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
        }
    
        t = ""
        i = 0
        while i < len(encodedStr):
            c = encodedStr[i]
            if c == '+':
                t += ' '
            elif c == '%':
                digit_high, digit_low = encodedStr[i + 1], encodedStr[i + 2]
                i += 2
                if digit_high in hex_values and digit_low in hex_values:
                    v = hex_values[digit_high] * 16 + hex_values[digit_low]
                    t += chr(v)
                else:
                    raise ValueError("Invalid encoding")
            else:
                t += c
            i += 1
        return t

encodedStr = 'poetName=Alfred%2C+Lord+Tennyson&nPoems=20'
print('Encoded string:', encodedStr)
print(CgiEnDecoder.CgiDecode(encodedStr))