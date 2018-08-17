#查找插入位置
##在一个已经排序的队列中，若target已存在队列中，返回index，否则插入一个合适的位置，并返回index
def searchInsert(nums,target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    #######运行速度最慢的一个版本
    # if target in nums:
    #     return nums.index(target)
    # elif target<nums[0]:
    #     return  0
    # elif target>nums[len(nums)-1]:
    #     return len(nums)
    # else:
    #     for i in range(len(nums)-1):
    #         if nums[i]<target and nums[i+1]>target:
    #             return i+1

########这个采用的是二分法，速度更快，我在写上一个代码的时候，就有想过用二分法来着，可是中间的min、max弄混容易
    # min=0
    # max=len(nums)-1
    # middle=nums[(min+max)//2]
    # while min+1<max:
    #     if middle<target:
    #         min=(min+max)//2
    #         middle=nums[(min+max)//2]
    #     elif middle>target:
    #         max=(min+max)//2
    #         middle=nums[(min+max)//2]
    #     else:return (min+max)//2
    # if nums[max]<target:
    #     return max+1
    # elif nums[min]<target:
    #     return max
    # else:
    #     return min
    #
######更快速的二分查找方法
    left,right=0,len(nums)
    while left<right:
        mid=(right-left)//2+left
        if nums[mid]>=target:
            right=mid
        else:
            left=mid+1
    return left

if __name__=="__main__":
    nums=[1,3,5,7]
    target=3
    print(searchInsert(nums,target))