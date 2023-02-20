class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #O(n) time complexity using this approach
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, counter in count.items():
            freq[counter].append(num)   
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res