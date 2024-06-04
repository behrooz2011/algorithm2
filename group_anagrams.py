
"""Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters."""
""" 
     Study:

 {
  "aet": ["eat", "tea", "ate"],
  "ant": ["tan", "nat"],
  "abt": ["bat"]
}
"""
def groupAnagram(arr):
    obj = {}
    res = []
    for i in range(len(arr)):
        if(''.join(sorted(arr[i])) not in obj):
            obj[''.join(sorted(arr[i]))] = []
    for i in range(len(arr)):
        if(''.join(sorted(arr[i])) in obj):
            obj[''.join(sorted(arr[i]))].append(arr[i])
    for val in obj:
        res.append(obj[val])

    print(res)
groupAnagram(["eat","tea","tan","ate","nat","bat"])
            