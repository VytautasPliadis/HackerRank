from collections import OrderedDict


def user_input():
    input_list = input().split()
    net_price = input_list[-1]
    input_list.pop()
    item_name = ' '.join(input_list)
    return item_name, net_price


def calculator(ordered_dict, item_name, net_price):
    ordered_dict[item_name] += int(net_price)


def main():
    ordered_dict = OrderedDict()
    number_bought_items = int(input())
    if not 1 < number_bought_items <= 100:
        raise ValueError

    for _ in range(number_bought_items):
        item_name, net_price = user_input()
        ordered_dict.setdefault(item_name, 0)
        calculator(ordered_dict, item_name, net_price)

    for item, price in ordered_dict.items():
        print(item, price)


if __name__ == '__main__':
    main()

'''
4
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
'''
