# Given a 32-bit signed integer, reverse digits of an integer.
# Input: 123
# Output: 321
# Input: -123
# Output: -321
# Input: 120
# Output: 21

# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
###########数字反向输出 整数数字的取值范围是[−2^31,  2^31 − 1].

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    # ###我的写法，效果不好，就占13%
    # s=int(str(abs(x))[::-1])
    # if s>2**31-1 or s<-2**31:
    #     return 0
    # elif x>=0:
    #     return s
    # else:return -s

#############运行速度56s，占93.80%
    x_str = str(x)
    handle = int(x_str[::-1] if not x_str.startswith('-') else '-' + x_str[::-1][:-1])
    if abs(handle) < 0xffffffff / 2:
        return handle
    return 0


    # #########速度最快的版本是
    # print((x > 0),(x < 0),((x > 0) - (x < 0)))
    # result = ((x > 0) - (x < 0)) * int(str(abs(x))[::-1]) ###其中((x > 0) - (x < 0)) 输出的值为+1或者-1，（x>0）、 (x < 0)要么为true要么为flase，且不可能同时为true或flase
    # return result if result >= -2 ** 31 and result < 2 ** 31 else 0

if __name__=="__main__":
    x=-199946699
    print(reverse(x))