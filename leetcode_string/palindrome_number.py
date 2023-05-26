class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        y=x[::-1]
        if x==y:
            return True
        return False 
if __name__=="__main__":
    s=Solution()
    if s.isPalindrome(123):
        print("yes")
    else:
        print("no")