def twoSum(nums,target):
    res = []
    obj = {}
    for i in range(len(nums)):
        if nums[i] not in obj:
            obj[nums[i]] = [i]
        else:
            obj[nums[i]].append(i)
        if target - nums[i] in obj and obj[target - nums[i]][0] != i: #to exclude itself e.x [3,3], target 0
            res.append([i,obj[target - nums[i]][0]])
    print(obj)
    print(res)
    return res[0]

