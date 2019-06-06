# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:02:31 2019

@author: G2
"""
from Fuzzer import Fuzz

class HeartBeatBug:
    systemMemory = ''
    uninitializedSystemMemory = 'OtherMemoryOperations'
    
    def __init__(self):
        self.systemMemory = ('<space for reply>' + Fuzz.Fuzzer(100)
        + '<secret-certificate>' + Fuzz.Fuzzer(100)
        + '<secret-key>' + Fuzz.Fuzzer(100) + '<other-secrets>')
    
    def Respond(self, response, length):
        try:
            self.systemMemory = response + self.systemMemory
            if len(self.systemMemory) < length:
                while len(self.systemMemory) < length:
                    self.systemMemory += self.uninitializedSystemMemory
            return self.systemMemory[0:length]
        except Exception as exc:
            print(exc)