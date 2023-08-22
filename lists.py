class ListModifier:
    def __init__(self):
        self.arr = []

    def insert(self, x, y):
        self.arr.insert(int(x), int(y))

    def print(self):
        print(self.arr)

    def remove(self, x):
        self.arr.remove(int(x))

    def append(self, x):
        self.arr.append(int(x))

    def sort(self):
        self.arr.sort()

    def pop(self):
        self.arr.pop(-1)

    def reverse(self):
        self.arr.reverse()

    def comand_checker(self):
        command, *number = input().split()
        if command == 'insert' and len(number) == 2:
            self.insert(number[0], number[1])
        elif command == 'print' and len(number) == 0:
            self.print()
        elif command == 'remove' and len(number) == 1:
            self.remove(number[0])
        elif command == 'append' and len(number) == 1:
            self.append(number[0])
        elif command == 'sort' and len(number) == 0:
            self.sort()
        elif command == 'pop' and len(number) == 0:
            self.pop()
        elif command == 'reverse' and len(number) == 0:
            self.reverse()



if __name__ == '__main__':
    arr = ListModifier()
    N = int(input())
    for _ in range(N):
        arr.comand_checker()


'''
7
insert 0 5
remove 5
append 3
append 2
sort
pop
print
'''