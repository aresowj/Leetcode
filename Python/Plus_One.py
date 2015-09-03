'''
Leetcode exercise
Written by aresowj

[Plus One]
Given a non-negative number represented as an array of digits, plus one to the number.
The digits are stored such that the most significant digit is at the head of the list.
'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype : List[int]
        """
        digits = digits[::-1]
        number = 0
        
        for i in range(0, len(digits)):
            number += digits[i] * (10 ** i)

        sum = number + 1
        result = []
        
        for i in str(sum):
            result.append(int(i))
            
        return result
