# Implement strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# 当needle一个空字符串时我们应该返回什么？在面试中这是一个很好的问题。
# 出于此问题的目的，当needle为空字符串时，我们将返回0 。这与C的  strstr（）和Java的  indexOf（）一致。
def strStr(haystack,needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    ######这个方法是调用包，速度在40ms，占64.68%
    # if len(needle)==0:
    #     return 0
    # return haystack.find(needle)

    ##运行最快的方法，是我原先有想到的切片的方法，但我的那个在下标处理出现问题了
    if not needle:
         return 0
    lenh=len(haystack)
    lenn=len(needle)
    if lenh<lenn:
        return -1
    for i in range(lenh-lenn+1): ##我的错误主要在这个len怎么定，这里是长的-短的+1
        if haystack[i:lenn+i]==needle:
            return i
    return -1


if __name__=="__main__":
    haystack = "hello"
    needle = "lo"
    print(strStr(haystack,needle))