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




############ Solution 2 ###################
"""
Let's break down how this solution works:

We use a sliding window approach where we maintain:

A window defined by left and right pointers
A dictionary to count characters in the current window
max_count to track the count of most frequent character in window


For each position of right pointer:

We add the new character to our count
Update max_count if necessary
Check if our window is valid (requires ≤ k replacements)
If invalid, shrink window from left
Update max_length if current window is longer


The key insight is that for any window:

Window size - count of most frequent char = minimum replacements needed
If this exceeds k, window is invalid


Time complexity: O(n) where n is length of string
Space complexity: O(1) since we store at most 26 characters

Let's test it with the examples:
"""
def longest(s,k):
    # Dictionary to store character counts in current window
    char_count = {}
    
    # Variables to track window and result
    max_length = 0
    max_count = 0
    left = 0
    
    # Iterate through the string with right pointer
    for right in range(len(s)):
        # Add new character to count
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # Update max_count - the count of most frequent char in current window
        max_count = max(max_count, char_count[s[right]])
        
        # Current window size - max_count gives us number of chars to be replaced
        # If this exceeds k, shrink window from left
        window_size = right - left + 1
        if window_size - max_count > k:
            # Remove leftmost character from count
            char_count[s[left]] -= 1
            left += 1
        
        # Update max_length with current window size
        max_length = max(max_length, right - left + 1)
    
    return max_length