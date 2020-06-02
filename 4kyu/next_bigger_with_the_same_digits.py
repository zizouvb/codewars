def is_anagram(a,b):
    return int("".join(sorted(list(str(a))))) ==int("".join(sorted(list(str(b))))) 
def next_bigger(n):
    my_number_list = list(str(n))
    max_number_list = sorted(my_number_list,reverse=True)
    max_number = int("".join(max_number_list))
    i=int("".join(my_number_list))+1
    print(i)
    print(max_number)
    while i<=max_number:
        if is_anagram(i,max_number):
            return i
        i+=1
    return -1
