from collections import deque


def deque_operation(que, operation):
    operations_mapping = {
        'append': que.append,
        'appendleft': que.appendleft,
        'pop': que.pop,
        'popleft': que.popleft,
    }

    if operation[0] in operations_mapping:
        func = operations_mapping[operation[0]]
        if len(operation) > 1:
            func(operation[1])
        else:
            func()
    else:
        raise ValueError(f'Invalid operation: {operation}')

def main():
    d = deque()
    number_operations = int(input())
    if 1 < number_operations <=100:
        for _ in range(number_operations):
            operation = input().split()
            deque_operation(d, operation)

        print(*d)


if __name__ == '__main__':
    main()
