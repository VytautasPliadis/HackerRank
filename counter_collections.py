from collections import Counter


def constraints_check(shoes_quantity, shoes_list, customers_number):
    if not 1 < shoes_quantity <= 1000 or not 1 < customers_number <= 1000:
        raise ValueError('Please enter valid shoes quantity of customers number')
    for i in shoes_list:
        if not 2 <= int(i) <= 20:
            raise ValueError('Please enter valid shoe size')


def customer_transaction(desired_shoe_nr, shoes_dict, willing_to_pay, revenue_from_shoes):
    if desired_shoe_nr in shoes_dict:
        if not 20 <= willing_to_pay <= 100:
            raise ValueError()
        shoes_dict[desired_shoe_nr] -= 1
        revenue_from_shoes += willing_to_pay
        if shoes_dict[desired_shoe_nr] == 0:
            shoes_dict.pop(desired_shoe_nr)
    return shoes_dict, revenue_from_shoes


if __name__ == '__main__':
    shoes_quantity = int(input())
    shoes_list = input().split()
    shoes_dict = Counter(shoes_list)
    customers_number = int(input())
    constraints_check(shoes_quantity, shoes_list, customers_number)
    revenue = 0

    for _ in range(customers_number):
        customer_shoe_and_cash = input().split()
        desired_shoe_nr = str(customer_shoe_and_cash[0])
        willing_to_pay = int(customer_shoe_and_cash[1])

        transaction = customer_transaction(desired_shoe_nr, shoes_dict, willing_to_pay, revenue)
        revenue = transaction[1]
        shoes_dict = transaction[0]

    print(revenue)
