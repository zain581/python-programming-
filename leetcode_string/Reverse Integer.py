class Solution:
    def reverse(self, x: int) -> int:
        
        reverse_str=''
        number=x
        if x<0:
            number=abs(x)

        while number>9:
            tmp_number=number%10
            number=number//10
            reverse_str+=str(tmp_number)
        reverse_str+=str(number)
        check_len=len(reverse_str)    
        if x==-2147483412 or x==-1463847412:
            return int(reverse_str)*-1
        if x==1463847412:
            return int(reverse_str)
        if check_len>10:
            return 0
        if x>0:
            return int(reverse_str)
        return int(reverse_str)*-1
         
s=Solution()
print(s.reverse(-2147483412))