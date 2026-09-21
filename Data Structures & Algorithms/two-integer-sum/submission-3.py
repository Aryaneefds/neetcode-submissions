class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = set()

        for i,a in enumerate(nums):
            if target - a in hashset:
                t1 = i
                t2 = nums.index(target-a)
                return [t2,t1]
            else:
                hashset.add(a)
        