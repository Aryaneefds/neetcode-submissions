class Solution:

    def encode(self, strs: List[str]) -> str:
        ss = ""
        for s in strs:
            size= len(s)
            ss+=str(size)
            ss+='#'
            ss+=s
        return ss
        


    def decode(self, s: str) -> List[str]:
        l = 0
        k = []
        
        while l<len(s):

            a = ''
            while s[l]!='#' and l<len(s)-1 :
                a+=s[l];
                l+=1;
            lg = int(a)
            l+=1;
            k.append(s[l:l+lg])
            l=l+lg

        return k
                






