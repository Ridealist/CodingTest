"""
https://leetcode.com/problems/roman-to-integer/
"""

class Solution:
    
    roman_dic = {}
    val1 = [1, 5]
    for i, r in enumerate(['I', 'V', 'X', 'L', 'C', 'D', 'M']):
        roman_dic[r] = val1[i%2]*(10**(i//2))
    
    roman_sub_dic = {}
    val2 = [4, 9]
    for i, r in enumerate(['IV', 'IX', 'XL', 'XC', 'CD', 'CM']):
        roman_sub_dic[r] = val2[i%2]*(10**(i//2))


    def romanToInt(self, s: str):
        answer = 0
        l = len(s)
        i = 0
        while i < l:
            if i <= l-2:
                two = s[i] + s[i+1]
                if two in self.roman_sub_dic:
                    answer += self.roman_sub_dic[two]
                    i += 2
                else:
                    answer += self.roman_dic[s[i]]
                    i += 1
            else:
                answer += self.roman_dic[s[i]]
                i += 1

        return answer