from collections import Counter
def minWindow(s,t):
    countT = {}
    left = 0
    obj = {} # arr values containing indexes
    countS = {}
    
    for i in range(len(t)):
        countT[t[i]] = 1 + countT.get(t[i] , 0)
    print("countT: ",countT)
    for right in range(len(s)):
        if s[right] not in t:
            left += 1
        else:#populate s-related variable based on elements in t
            countS[s[right]] = 1 + countS.get(s[right] , 0)
            # obj[s[right]] = countT.get()
            if s[right] not in obj:
                obj[s[right]] = [right]
            else:
                obj[s[right]].append(right)
        #check if the object has the elements of countT
        # or similarly,  countS values are bigger or equal to countT values
    print("countS: ",countS)
    if Counter(countT) <= Counter(countS):
            print(s[left: right+1])
print(minWindow("ADOBECODEBANC", "ABC"))# not completed yet