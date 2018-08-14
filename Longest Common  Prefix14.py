#####获取一个list中的字符的最长字符串前缀，如果没有前缀，返回""
# Input: ["flower","flow","flight"]
# # Output: "fl"
# # Input: ["dog","racecar","car"]
# # Output: ""
# # Explanation: There is no common prefix among the input strings.
# 输入的字符从a-z

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    # prefix=''
    # if not strs:
    #     return ""
    # min_len=len(min(strs,key=len))
    # if min_len==0:
    #     return ""
    # n=0
    # n_chars=set(a[0] for a in strs)
    # while len(n_chars)==1 and n<min_len:
    #     prefix+=strs[0][n]
    #     n+=1
    #     if n==min_len:
    #         break
    #     n_chars=set(a[n] for a in strs)
    # return prefix

#########这个代码运行速度在85%左右，使用迭代器里中的一个内置函数
   #  if not strs:
   #      str = ''
   #      return str
   #  from itertools import takewhile
   # ### print(list(takewhile(lambda x: len(set(x)) == 1, zip(*strs))))  运行结果是[('f', 'f', 'f'), ('l', 'l', 'l')]
   #  max_pre_len = len(list(takewhile(lambda x: len(set(x)) == 1, zip(*strs))))  ###len([],zip(*str)) 是将几个list 中的元素分别按照对应位置进行组合，[('f','f''f'),('l','l','l')]
   #                                                                               ####takewhile() 就是一个运算迭代器， 整句话目的就是将符合条件的前缀通过迭代形式生成list，并且通过取其len得知最长前缀有几个字母组成，以便返回
   #  str = strs[0][:max_pre_len]
   #  return str

###########运行速度最快的代码
    if not strs:
        return ""
    #print(enumerate(zip(*strs))) ### zip(*strs)是把list中的每个str的每个字母压缩成这种('f', 'f', 'f')、('l', 'l', 'l')等形式
    for i, ch in enumerate(zip(*strs)):
        print(i,ch)
        if len(set(ch)) != 1:
            return strs[0][:i]
    else:
        return min(strs, key=len)

if __name__=="__main__":
    strs= ["flower","flow","flight"]
    print(longestCommonPrefix(strs))