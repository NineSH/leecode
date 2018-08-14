# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
# 判断一个整数是否是回文整数
# Input: 121
# Output: true
# Input: -121
# Output: false
# Input: 10
# Output: false

def isPalindrome(x):
    ###运行速度只占5.73%
    # if str(x)==(str(x)[::-1]):
    #     return True
    # else:
    #     return False

    ###运行速度最快的代码 我感觉和我那个没什么差别呀
    x_list=[i for i in str(x)]
    if x_list==x_list[::-1]:
        return True
    else:
        return False
if __name__=="__main__":
    x=101
    print(isPalindrome(x))