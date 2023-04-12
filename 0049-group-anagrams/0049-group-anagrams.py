class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)
        
        for str in strs:
            count = [0] * 26 #to account for all the characters a - z
            for char in str:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(str)
        return res.values()