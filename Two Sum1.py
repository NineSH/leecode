# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# 给定一个整数数组，从数组中找两个数值使其相加等于目标数字，并返回其在数组的位置 主要每个target只有一个解决办法
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# eg.nums=nums = [2,7,11,15]，target = 9，
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def twoSum(nums,target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # ##### 从前往后找一对符合条件的整数，用字典的形式进行存储。
    # 运行速度40是，占83.42%
    # dict = {}
    # for i in range(len(nums)):
    #     x = nums[i]
    #     if target - x in dict:#判断是否有匹配的值在字典中，如果有返回下标
    #         return (dict[target - x], i)
    #     dict[x] = i #将每个x与其对应下标存成字典形式，然后用value来找是否有匹配的

##########这个算法采用的是list自带的index来找第一个匹配数的下标
   ###这个运行速度慢了1088s.占36%，个人感觉好像使用字典的话速度会快很多
    for i,num in enumerate(nums):
        pair=target-num
        if pair in nums[i+1:]:
            return [i,nums.index(pair,i+1)]
    return None
if __name__=="__main__":
    nums=[2,7,11,15]
    target=13
    print(twoSum(nums,target))