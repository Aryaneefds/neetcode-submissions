class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n,0) + 1;
        m2 = {}
        for key,val in hashmap.items():
            m2[val]= m2.get(val, [])
            m2[val].append(key)

        result = []

        for freq in range(len(nums), 0 , -1):
            if freq in m2:
                for number in m2[freq]:
                    result.append(number)

                    if (len(result)==k):
                        return result
                
    



        