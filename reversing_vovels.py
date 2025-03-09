class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: strv
        :rtype: str
        """
        vowels = 'aeiouAEIOU'
        s = list(s)
        first,last = 0,len(s)-1

        while first<last:
            if s[first] not in vowels:
                first+=1
            elif s[last] not in vowels:
                last-=1
            else:
                s[first] , s[last] = s[last], s[first]
                first = first+1
                last = last-1

        return ''.join(s)
    
solution = Solution()
print(solution.reverseVowels("IceCreAm"))
print(solution.reverseVowels("leetcode"))