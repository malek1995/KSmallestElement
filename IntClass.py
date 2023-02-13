"""
This is a custom implementation of the int class that overrides two methods for comparison,
 __lt__ (less than) and __gt__ (greater than), and keeps track of the number of times these methods are called
 by storing it as a class variable count. The resetCount method is a static method that resets the count to 0.
"""


class Int(int):
    count = 0

    # smaller than
    def __lt__(self, other):
        Int.count += 1
        return int.__lt__(self, other)

    # greater than
    def __gt__(self, other):
        Int.count += 1
        return int.__gt__(self, other)

    @staticmethod
    def resetCount():
        Int.count = 0
