# -*- coding: utf-8 -*-
"""
Created on Mon May 20 18:29:08 2019

@author: AG
"""
import time

def clock():
    try:
        return time.perf_counter()  # Python 3
    except:
        return time.clock()         # Python 2

class Timer(object):
    # Begin of `with` block
    def __enter__(self):
        self.start_time = clock()
        self.end_time = None
        return self

    # End of `with` block
    def __exit__(self, exc_type, exc_value, tb):
        self.end_time = clock()

    def elapsed_time(self):
        """Return elapsed time in seconds"""
        if self.end_time is None:
            # still running
            return clock() - self.start_time
        else:
            return self.end_time - self.start_time