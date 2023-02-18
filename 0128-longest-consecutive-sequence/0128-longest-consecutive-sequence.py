class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #This has space and time complexity of O(n) using the hashset data structure
        hashset = set(nums)
        longest = 0
        for num in nums:
            if (num - 1) not in hashset:
                length = 0
                while (num + length) in hashset:
                    length += 1
                longest = max(length, longest)
        return longest