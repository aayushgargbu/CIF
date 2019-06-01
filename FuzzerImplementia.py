# -*- coding: utf-8 -*-
"""
Created on Tue May 21 13:23:12 2019

@author: AG
"""

from Fuzzer import Fuzz
import os
import tempfile

basename = "TempFuzz.txt"
tempdir = tempfile.mkdtemp()
FILE = os.path.join(tempdir, basename)
print(FILE)

fileData = Fuzz.Fuzzer(100)
with open(FILE, "w") as f:
    f.write(fileData)

fileContents = open(FILE).read()
print(fileContents)
assert(fileData == fileContents)