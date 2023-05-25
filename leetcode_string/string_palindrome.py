# max len palindrome in string
class Solution:
    def longestPalindrome(self, s: str) -> str:
        list_of_palindrome=[]
        check_full_string=s[::-1]
        if check_full_string==s:
            return check_full_string
        for i in range(0,len(s)):
            tmp_str=''
            try:
                for j in range(i,len(s)):
                    tmp_str=tmp_str+s[j]
                    reverse_str=tmp_str[::-1]
                    #print(tmp_str,reverse_str)
                    if tmp_str==reverse_str:
                        print(tmp_str,reverse_str)
                        list_of_palindrome.append(reverse_str)
                        continue
                 
                    second_tmp=tmp_str+s[j+1]
                    second_reverse=second_tmp[::-1]
                    if second_tmp!=second_reverse:
                        continue
            except:
                pass
        max_length_string = max(list_of_palindrome, key=len)
        return max_length_string


            

        