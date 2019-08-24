class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        
        res = ''
        for i in range(len(nums)):
            while num >= nums[i]:
                res += romans[i]
                num = num - nums[i]
            
        return res


s = Solution()
print(s.intToRoman(8))
