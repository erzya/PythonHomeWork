#Task1
def get_min_el_out_of_array(A):
    max_in_range = 100001
    for elem in range(1,max_in_range):
        try:
            index_value = A.index(elem)
        except ValueError:
            return elem
A = [1, 3, 6, 4, 1, 2,-8,16,-80,-1,0,-34,-20,-9,-10,45,3,5]
print(get_min_el_out_of_array(A))

#Task2
def get_max_binary_gap(N):
    max_bin_gap=0
    for elem in N:
        arr_elem_bin_convert = str(format(elem,'b')).split('1')
        for char in arr_elem_bin_convert[1:-1]:
            if len(char) > max_bin_gap:
                max_bin_gap = len(char)
    return max_bin_gap

print(get_max_binary_gap([1,2,147,483,647]))

#Task3
def shift_array_to_right(A,K):
    reverse_array = A
    if K < 0 and K > 100:
        return
    elif K==0:
        return A
    else:
        for el in range(0,K):
            reverse_array.insert(0,reverse_array.pop())
    return reverse_array

A = [3, 8, 9, 7, 6]
K = 3
print(shift_array_to_right(A,K))

#Task4
def get_factor_amount(K):
    factor_amount = 0
    if K >1:
        for el in range(1,K+1):
            if K%el == 0:
                factor_amount +=1
        return factor_amount
    elif K==1:
        return 1
    else:
        return

print(get_factor_amount(25))

#Task5
def get_lenght_of_longest_pssw(S):
    max_length = -1
    pssw_array = S.strip().split()
    if len(pssw_array) >0:
        for elem in pssw_array:
            numbers = sum(c.isdigit() for c in elem)
            letters = sum(c.isalpha() for c in elem)
            others =len(elem) - numbers - letters
            if others == 0 and letters%2 == 0 and numbers%2 != 0:
                if len(elem) > max_length:
                    max_length = len(elem)
    return max_length
print(get_lenght_of_longest_pssw("test   ?xy1 PR#f12 *^&^"))

#Task6
def is_properly_nested_string(S):
    reuslt = 0
    if len(S) == 0:
        reuslt = 1
    else:
        splitted_by_open = S.split("(")
        splitted_by_close = S.split(")")
        if len(splitted_by_open) == len(splitted_by_close):
            reuslt = 1
    return reuslt
print(is_properly_nested_string("(()(())())"))
