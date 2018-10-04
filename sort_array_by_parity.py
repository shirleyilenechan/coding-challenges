def sort_array_by_parity(A):
    even_list = [num for num in A if num % 2 == 0]
    odd_list = [num for num in A if num % 2 != 0]
    return even_list + odd_list
