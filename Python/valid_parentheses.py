# -*- coding: utf-8 -*-

"""Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid. The brackets must close in the correct 
order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opens = []
        d = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for c in s:
            if c in ['(', '{', '[']:
                opens.append(c)
            elif not opens or d[opens[-1]] != c:
                return False
            else:
                opens.pop()
        return False if opens else True

