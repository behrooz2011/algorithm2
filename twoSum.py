def twoSum(nums,target):
    result = []
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
    return result
print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))

print("complexity n")
def twoS(x,target):
  obj={}
  arr=[]
  for index,val in enumerate(x):
    obj[val]=val
    if target - val in obj and x.index(target - val) != index:
      # arr.append([index,x.index(target-val)])
      arr.append(index)
      arr.append(x.index(target - val))
  return arr
print(twoS([1,2,2,3,4,3,5,1,7],9))
print(twoS([2,7,11,15],9))
print(twoS([3,2,4,4],6))
