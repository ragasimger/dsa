class Solution(object):
    def removeDuplicates(self, nums):
        # return len(set(nums))
        num = sorted(nums)
        print(num)
        set_num = set(num)
        print(set_num)
        length = len(set_num)
        return length

x = Solution()
nums = [1,1,2]
b = x.removeDuplicates(nums=nums)
print(b)
