class Solution(object):
    def numberOfGoodPaths(self, vals, edges):
        if len(vals)==0:
            return 0
        counter=0   
        
        flag=True
        for i in range(0,len(vals)):
            
            try:
                if vals[i]==vals[i+1]:
                    counter+=1
                    flag=False
                    # print("flase")
            except:
                pass
            for j in range(0,len(vals)):
                
                if vals[i]>=vals[j]:
                    if flag:
                        counter+=1
                    if i ==j or vals[i]==vals[j]:
                        flag=True                        
        return counter//2
# print(good_tree([1,3,2,1,3],[[0,1],[0,2],[2,3],[2,4]]))
# good_tree([1],[])
# good_tree([1,3,2,1,3],[])
s=Solution()
print(s.numberOfGoodPaths([2,2,5,5],[[1,0],[0,2],[3,2]]))
print(s.numberOfGoodPaths([1,1,2,2,3],[[0,1],[0,2],[2,3],[2,4]]))
print(s.numberOfGoodPaths([1,3,2,1,3],[[0,1],[0,2],[2,3],[2,4]]))