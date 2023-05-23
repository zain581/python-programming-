"""Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M."""
def intToRoman( num: int) -> str:
    Mapping_Symbols={1:"I",5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
    Defulat_Symbols={4:"IV",9:"IX", 49:"IL", 99:"IC", 499:"ID"}
    if num in Mapping_Symbols :
        return Mapping_Symbols[num]
    if num in Defulat_Symbols:
        return Defulat_Symbols[num]
    Mapping_list={}
    #list for key mapping
    List_keys=[]
    #calclaute difference between each point 
    for i in Mapping_Symbols.keys():
        Mapping_list[abs(num-i)]=i
    print(Mapping_list)
    len_loops=len(Mapping_list.keys())
    module_list={}
    for module in Mapping_Symbols.keys():
        number=num%module
        if number==num:
            continue
        module_list[module]=number
    keys_arrow={}
    for k in module_list.keys():
        keys_arrow[k]=num-k
    sum_total=0
    value_match=[]
    print(keys_arrow)
    for l in keys_arrow.keys():
        sum_total+=l
        value_match.append(Mapping_Symbols[l])
        if sum_total==num:
            break
        elif sum_total>num:
            print("sum total is larger")
            sum_total-=l
    if sum(keys_arrow.keys())==num:
        return value_match
    
    max_number=num-sum(keys_arrow.keys())
    real_number=value_match[::-1]
    tmp_str=''
    for i in real_number:
        tmp_str+=i
    test_str=max_number*"I"
    tmp_str+=test_str
    return tmp_str

    
print(intToRoman(234))