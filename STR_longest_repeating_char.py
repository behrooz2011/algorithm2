"""
424. Longest Repeating Character Replacement
Solved
Medium
Topics
Companies
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
"""
def characterReplacement(s,k):
    count = {}
    res = 0
    left = 0
    for right in range(len(s)):
        count[s[right]] = 1 + count.get(s[right], 0)
        while (right - left + 1) - max(count.values()) > k: #if the length of the window gets bigger than the most frequent char:
            count[s[left]] -= 1
            left += 1
        res = max(res, right - left + 1)
    return res
"""
tip:
move to the right as long as the length of the sliding window minus the most frequent char is less or equal to k.
if not, move the left pointer to the right and check the condition again (hence the while loop as opposed to an if statement) 
"""