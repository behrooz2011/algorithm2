def groupAnagrams(arr):
    obj = {}
    for i in range(len(arr)):
       if(''.join(sorted(arr[i])) not in obj):
         obj[''.join(sorted(arr[i]))] = [arr[i]]
       else:
        obj[''.join(sorted(arr[i]))].append(arr[i])
    return list(obj.values())
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))