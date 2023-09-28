from itertools import combinations

user_input = input()
string_combine, len_combinations = user_input.split()
string_combine = ''.join(sorted(string_combine))
len_combinations = int(len_combinations)
if not string_combine.isupper() or len_combinations > len(string_combine):
    raise ValueError

for i in range(1, len_combinations + 1):
    combs = list(combinations(string_combine, i))
    for _ in combs:
        print(*_, sep='')