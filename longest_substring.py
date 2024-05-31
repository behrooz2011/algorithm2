"""Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring."""


def longest(s):
    slide = ""
    result =""
    for i in range(len(s)):
        if s[i] not in slide:
            slide += s[i]
            result = slide if len(slide) > len(result) else result #ternary

        else:
            slide = slide[slide.index(s[i])+1:i] + s[i] #(up to) the repetitive value deleted, new string added
            # print("slide:",slide)
            result = slide if len(slide) > len(result) else result #ternary
    return result


print(longest("abca"))
print(longest("abbbca"))
print(longest("abcabbcadfbb"))
print(longest("abcabcbb"))