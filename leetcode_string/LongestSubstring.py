class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        if  s==" " or len(s)==1:
            return 1
        if len(s)==2 and s[0]!=s[1]:
            return 2
        if s=="":
            return 0
        test_str=""
        final_str=[]
        for j in range(0,len(s)):
            
            for i in range(j,len(s)):
                if s[i] in test_str:
                    final_str.append(test_str)
                    test_str=s[j]
                    print(test_str)
                    break
                else:
                    test_str=test_str+s[i]
        maxium=0
        final_str.append(test_str)
        for i in final_str:
            if maxium<len(i):
                maxium=len(i)
        print(final_str)
        return maxium


