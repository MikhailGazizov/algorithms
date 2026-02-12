'''
Palindrome Number:
Create a function which will define whether it is a palindrome (example: 12321 is 12321 if you write it backwards) or not.
No usage of Int to Str conversion.

Input: Integer number (x) between -2^31 and 2^31 - 1
Output: Boolean
'''

from math import ceil, log10


class IsPalindrome:

    @staticmethod
    def solution_1(x):

        if x <= 0:
            return False

        x_len = ceil(log10(x + 1))

        for i in range(x_len // 2 + 1):
            if (x // 10 ** i) % 10 != (x // 10 ** (x_len - i - 1)) % 10:
                return False
        return True

    @staticmethod
    def solution_2(x):

        if x <= 0:
            return False

        cur = 0
        y = x

        while y > 0:
            cur = cur*10 + y%10
            y = y//10

        return cur == x

cases = [
    IsPalindrome.solution_2(10),
    IsPalindrome.solution_2(11),
    IsPalindrome.solution_2(2),
    IsPalindrome.solution_2(-1),
    IsPalindrome.solution_2(101),
    IsPalindrome.solution_2(111),
    IsPalindrome.solution_2(1234)
]

print(cases)
