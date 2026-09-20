class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for a in nums:
            freq[a] = freq.get(a,0) + 1;

        for a in nums:
            if( freq[a]>1):
                return True

        return False                        
        