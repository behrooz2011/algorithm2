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


################ part 2: unique values instead of indexes ########################
def twoSum(nums,target):
        res = []
        obj = {}
        my_set = set()
        for i in range(len(nums)):
            if nums[i] not in obj:
                obj[nums[i]] = [i]
            else:
                obj[nums[i]].append(i)
            if target - nums[i] in obj and obj[target - nums[i]][0] != i:
                # res.append([i,obj[target - nums[i]][0]])
                my_set.add(tuple( sorted([nums[i], nums[obj[target - nums[i]][0]]]) ))
        print(obj)
        print("my_set",my_set)
        print([list(item) for item in my_set])
        # print(res)
        # return res[0]
twoSum([0,1,-2,0,2,1,-1,-1,-2,2],0)
twoSum([3,3],6)

