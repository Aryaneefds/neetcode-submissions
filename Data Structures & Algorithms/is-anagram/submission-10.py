class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        hashmap1 = {}
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
           #     print(i)
                hashmap[s[i]] = hashmap.get(s[i], 0) + 1
                hashmap1[t[i]] = hashmap1.get(t[i], 0) + 1

        for a in s:
            if(hashmap[a] != hashmap1.get(a,0)):
                return False

        return True
