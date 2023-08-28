cube = lambda x: x ** 3

def fibonacci(number_of_times):
    fibonacci_list = [0, 1]
    for _ in range(max(0, number_of_times - 2)):
        fib_nr = fibonacci_list[-2] + fibonacci_list[-1]
        fibonacci_list.append(fib_nr)
    return fibonacci_list[:number_of_times]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
