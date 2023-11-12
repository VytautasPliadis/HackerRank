def angryProfessor(k, a):
    attendance = [x for x in a if x <= 0]
    return "YES" if len(attendance) < k else "NO"


if __name__ == '__main__':
    t = int(input())
    summary = list()

    for _ in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        a = list(map(int, input().rstrip().split()))
        summary.append(angryProfessor(k, a))

    print(*summary, sep='\n')

'''
2
4 3
-1 -3 4 2
4 1
-1 -3 4 2
'''
