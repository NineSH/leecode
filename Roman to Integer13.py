# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
# Input: "III"
# Output: 3
# Input: "IV"
# Output: 4
# Input: "LVIII"
# Output: 58
# Explanation: C = 100, L = 50, XXX = 30 and III = 3.
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
##总的来说就是有个规则，然后需要将罗马字母写出其对应的数字

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    rdict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}  ##是用字典来记录一一对应关系
    num = i = 0
    while (i<=len(s)-1):
        if i==len(s)-1:###必须加入这一个判断句，不然会出现i溢出的情况
            num += rdict[s[i]]
            return num
        elif rdict[s[i]] < rdict[s[i + 1]]:
            num = num + rdict[s[i + 1]] - rdict[s[i]] ####关键是找出4、9系列的数字要怎么根据已知的来表示，可以发现是大字母对应值减去小字母对应值
            i = i + 2
        else:
            num += rdict[s[i]]
            i = i + 1
    return num
if __name__=="__main__":
    s="MCMXCIV"
    print(romanToInt(s))