# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# 去重
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

def removeDuplicates(nums):
    if not nums:
        return 0
    l2=list(set(nums))
    print(l2)
    return len(l2)
def removeDuplicates1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    M = {}
    p = 0
    for i, n in enumerate(nums):
        if n not in M:
            nums[p] = n
            p += 1
            M[n] = True
    return p

if __name__=="__main__":
    nums=[1,1,2]
    nums1=[0,0,1,1,1,2,2,3,3,4]
    print("len=",removeDuplicates(nums))
    print("len1=", removeDuplicates(nums1))
    print(removeDuplicates1(nums))