# -*- coding: utf-8 -*-
"""
Created on Tue May 21 13:01:07 2019

@author: AG
"""

import random

class Fuzz:
    
    def Fuzzer(max_length=100, char_start=32, char_range=32):
        """A string of up to `max_length` characters
           in the range [`char_start`, `char_start` + `char_range`]"""
        string_length = random.randrange(0, max_length + 1)
        #print('string_length:', string_length)
        out = ""
        for i in range(0, string_length):
            randChr = chr(random.randrange(char_start, char_start + char_range))
            #print('randChr:', randChr, ', ascii:', ord(randChr))
            out += randChr
        return out
    
    def CrashIfExceeds(fuzzStr, max_length):
        if len(fuzzStr) > max_length:
            raise ValueError

#print(Fuzz.Fuzzer())
#print(Fuzz.Fuzzer(1000, ord('a'), 26))

for i in range(100):
    mxLength = random.randrange(1, 200)
    print('mxLength:', mxLength)
    fuzzStr = Fuzz.Fuzzer(mxLength)
    print('fuzzStr:', fuzzStr, ', length:', len(fuzzStr))
    Fuzz.CrashIfExceeds(fuzzStr, 150)