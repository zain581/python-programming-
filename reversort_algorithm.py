# effient algo for sorting the array or list
def reversort(L):
    # l=[4,3,2,1]
    len_list=len(L)
    count_total=0
    for i in range(0,len(L)):
        j=L.index(min(L[i:len_list]))
        count_total=count_total+i
        
        reverse_element(L,i,j)
        # print("list",j,l[j])
        # L[i],L[j]=L[j],L[i]
        
        # print(L)
    print(count_total)
def reverse_element(list,i,j):
    # print(i,j)
    # # list[i]=list[j]
    # print(list)
    print(list)
    list[i],list[j]=list[j],list[i]
    return list
if __name__=="__main__":
    reversort(L=[4,2,1,3])