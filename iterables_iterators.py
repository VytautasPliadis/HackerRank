import itertools

len_list_n = int(input())
char_list = input().strip().split()
num_indices_k = int(input())

if not (1 <= len_list_n <= 10) or not (1 <= num_indices_k <= len_list_n):
    raise ValueError

a_tuple_number = 0
total_tuple_num = 0

# Total combinations of char_list with num_indices_k
tuple_list = list(itertools.combinations(char_list, num_indices_k))
for c in comb_list:
    total_tuple_num += 1
    a_tuple_number += 'a' in c

probability_a = a_tuple_number / total_tuple_num
probability_a = round(probability_a, 4)
print(probability_a)















for c in tuple_list:
    a_tuple_number += 'a' in c
