# 括号符号匹配，判断是否输入正确
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
# Input: "()"
# Output: true
# Input: "(]"
# Output: false
# Input: "{[]}"
# Output: true

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) == 1: return False
    parentheses = {"(": ")", "[": "]", "{": "}"} ##也是采用字典的形式来记录，这样速度更快
    s1 = [] #使用一个辅助list，可以更好的判断是否完全匹配，而且不存在思考元素位置及个数是否溢出等问题
    for i in s:
        if i in parentheses.keys():
            s1.append(parentheses[i])
        elif i in s1:
            s1.pop()
        else:
            s1.append(i)
    if (len(s1) == 0):
        return True
    else:
        return False
if __name__=="__main__":
    s="()[]{}"
    print(isValid(s))