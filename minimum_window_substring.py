""" 76. Minimum Window Substring
Hard
Topics
Companies
Hint
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?"""
""" Not efficient due to N^2 time complexity"""
class Solution:
    def is_subset(self,dictA, dictB):
        for key, value in dictA.items():
            if key not in dictB or dictB[key] < value:
                return False
        return True
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ""
        word = ""
        count = {}
       
        result = []
        for k in range(len(t)):
            count[t[k]] = count.get(t[k], 0) + 1
        for i in range(len(s)):
            for j in range(i,len(s)):
                word = s[i:j+1]
                # print(word)
                countS = {}
                for k in range(len(word)):
                    countS[word[k]] = countS.get(word[k],0) + 1
                # print("countS:",countS)
                # print("count:",count)
                if self.is_subset(count,countS):
                    result.append(word)

        # return result
        print("result",result)
        return "" if len(result) == 0 else min(result, key=len)
# solution = Solution()
# j =  solution.minWindow("ADOBECODEBANC","ABC")
# print(j)
print(Solution().minWindow("aaaaaaaaaaaabbbbbcdd","abcdd"))
###