# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.iven nums = [3,2,2,3], val = 3,
# Your function should return length = 2, with the first two elements of nums being 2.
# It doesn't matter what you leave beyond the returned length.


####功能:删除list中值为val的元素，并返回删除之后的list的长度
def removeElement(nums,val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    # count = nums.count(val)
    # print(count)  计数val在list中出现的次数，然后使用佛如循环进行删除 ，复杂度比下面那个方法更高一点
    while True:
        try:
            nums.remove(val)
        except:
            return len(nums)
if __name__=="__main__":
    nums=[0,1,2,2,3,0,4,2]
    val=2
    print(removeElement(nums,val))