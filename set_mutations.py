def mutation(mutation_name, main_set, user_set):
    match mutation_name:
        case 'update':
            main_set.update(user_set)
        case 'intersection_update':
            main_set.intersection_update(user_set)
        case 'symmetric_difference_update':
            main_set.symmetric_difference_update(user_set)
        case 'difference_update':
            main_set.difference_update(user_set)
        case _:
            raise ValueError("Unsupported mutation name")
    return main_set


main_set_num = int(input())
main_set = set(input().strip().split())

b_mutation_num = int(input())

for _ in range(b_mutation_num):
    # Collect input and do a mutation on set
    mutation_name, element_num = input().split()
    user_set = set(input().strip().split())
    main_set = mutation(mutation_name, main_set, user_set)

print(sum(map(int, main_set)))

'''
16
1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
4
intersection_update 10
2 3 5 6 8 9 1 4 7 11
update 2
55 66
symmetric_difference_update 5
22 7 35 62 58
difference_update 7
11 22 35 55 58 62 66
'''
