
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """

    # filtered_string = lower(''.join([char for char in s if char.isalnum()]))
    filtered_string = ''.join([char for char in s if char.isalnum()]).lower()
    phrase = ""
    for i in range(len(filtered_string)):
        if filtered_string[i] != filtered_string[len(filtered_string)-i-1]:
            phrase += filtered_string[i]
    return True if len(phrase) <= 1 else False
print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("Aba"))
print(isPalindrome("abba"))
print(isPalindrome("Ababba"))
print(isPalindrome("A"))
