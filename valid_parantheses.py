"""20. Valid Parentheses
Solved
Easy
Topics
Companies
Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'."""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if(len(s) % 2 == 1):
            return False
        obj = {"()":1,"{}":1,"[]":1}
        arr = [s[0]]
        for i in range(1,len(s)):
            arr.append(s[i])

            if ''.join(map(str, arr[-2:]))in obj:
                del arr[-2:]
        return True if len(arr) == 0 else False


        