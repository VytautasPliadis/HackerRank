from collections import defaultdict


def print_nested_list(nested_list):
    for inner_list in nested_list:
        if inner_list:
            print(*inner_list)  # Use unpacking to print elements within the same inner list
        else:
            print(-1)


def get_valid_input():
    value = input().strip()
    if not 1 <= len(value) <= 100:
        raise ValueError('Invalid input. Word length must be between 1 and 100 characters.')
    return value


if __name__ == '__main__':
    dd_list = defaultdict(list)

    try:
        m, n = map(int, input().strip().split())
        if not (1 <= m <= 10000) or not (1 <= n <= 100):
            raise ValueError("Both 'm' and 'n' must be in the range [1, 10000] and [1, 100], respectively.")
    except ValueError:
        raise ValueError("Invalid input. Please provide two integers separated by a space.")

    for _ in range(m):
        dd_list['A'].append(get_valid_input())
    for _ in range(n):
        dd_list['B'].append(get_valid_input())

    output_list = []

    for i in dd_list['B']:
        index_list = [index + 1 for index, value in enumerate(dd_list['A']) if value == i]
        output_list.append(index_list)

    # for i in dd_list['B']:
    # # index_list = []
    # #         for index, value in enumerate(dd_list['A']):
    # #             if value == i:
    # #                 index_list.append(index + 1)
    # #         output_list.append(index_list)

    print_nested_list(output_list)