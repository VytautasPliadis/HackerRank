from collections import defaultdict


def get_valid_input():
    value = input().strip()
    if not 1 <= len(value) <= 100:
        raise ValueError('Invalid input. Word length must be between 1 and 100 characters.')
    return value


if __name__ == '__main__':
    dd_list = defaultdict(list)
    A_B_input = input().strip().split()
    try:
        m, n = map(int, A_B_input)
        if not (1 <= m <= 1000) or not (1 <= n <= 100):
            raise ValueError("Both 'm' and 'n' must be in the range [1, 1000] and [1, 100], respectively.")
    except ValueError:
        raise ValueError("Invalid input. Please provide two integers separated by a space.")

    for _ in range(m):
        dd_list['A'].append(get_valid_input())
    for _ in range(n):
        dd_list['B'].append(get_valid_input())
