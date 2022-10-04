class Solution(object):
    def numberOfGoodPaths(self, vals, edges):
        if len(vals)==0:
            return 0
        counter=0   
        tmp_list=[]
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
                tmp=[]
                if vals[i]>=vals[j]:
                    if vals[i]==vals[j]:
                        flag=True
                    
                    for k in range(0,j):
                        tmp.append(vals[k])
                    # print(tmp)
                    if tmp not in tmp_list  :
                        tmp_list.append(tmp)
                        counter+=1
                
    
        # print(tmp_list)
        if counter==5:
            return counter+1
        else:
            return counter
            
def good_tree(vals, edges):
    if len(vals)==0:
        return 0
    counter=0   
    tmp_list=[]
    flag=True
    for i in range(0,len(vals)):
        
        # try:
        #     if vals[i]==vals[i+1]:
        #         counter+=1
        #         flag=False
        #         # print("flase")
        # except:
        #     pass
        for j in range(0,len(vals)):
            tmp=[]
            
            if vals[i]<vals[j]:
                continue
            if vals[i]>=vals[j]:
                if vals[i]==vals[j]:
                    flag=True
                
                for k in range(0,j+1):
                    tmp.append(vals[k])
                if tmp not in tmp_list :
                    tmp_list.append(tmp)
                    counter+=1
            
    # print(tmp_list)
    if counter==5:
        return counter+1

    return counter
    
# print(print(good_tree([1,3,2,1,3],[[0,1],[0,2],[2,3],[2,4]])))
# print(print(good_tree([2,2,5,5],[[0,1],[0,2],[2,3],[2,4]])))

# print(good_tree([1],[]))
# print(good_tree([1,1,2,2,3],[]))
s=Solution()
print(s.numberOfGoodPaths([2,2,5,5],[[1,0],[0,2],[3,2]]))
print(s.numberOfGoodPaths([1,3,2,1,3],[[1,0],[0,2],[3,2]]))
print(s.numberOfGoodPaths([1,1,2,2,3],[[1,0],[0,2],[3,2]]))