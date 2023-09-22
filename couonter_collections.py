from collections import Counter

# myList = [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]
# Counter(myList)
# Counter(myList).items()
# Counter(myList).keys()
# Counter(myList).values()


if __name__ == '__main__':
    shoes_quantity = int(input())
    shoes_list = input()
    customers_number = int(input())

    shoes_dict = Counter(shoes_list)