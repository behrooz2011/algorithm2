def containsDuplicate(nums):
    count = {}
    for i in range(len(nums)):
        count[nums[i]] = (count.get(nums[i]) or 0) + 1
        if count[nums[i]] > 1: return True
    return False
    # return True if max(count.values()) > 1 else False