from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if digits=="":
            return []
        Mapping_words={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        combination_list=[]
        for i in digits:
            combination_list.append(Mapping_words[int(i)])
        print(combination_list)
        # print(len(combination_list))
        output_list=[]
        combination_length = len(combination_list)
        print(combination_length)
        # Generate all possible combinations of characters of the given length
        combinations = [''.join(combination) for combination in product(*combination_list)]
        return combinations
if __name__=="__main__":
    s=Solution()
    print("combinattions ares{}".format(s.letterCombinations("786763723")))