from collections import Counter


def validate_input(shoes_quantity, customers_number, shoes_list):
    if not (1 < shoes_quantity <= 1000 and 1 < customers_number <= 1000):
        raise ValueError('Shoes quantity and customers number must be between 2 and 1000')
    if any(size < 2 or size > 20 for size in shoes_list):
        raise ValueError('Invalid shoe sizes. Sizes must be between 2 and 20.')


def customer_transaction(desired_shoe_nr, shoes_dict, willing_to_pay, revenue_from_shoes):
    if desired_shoe_nr in shoes_dict and 20 <= willing_to_pay <= 100:
        shoes_dict[desired_shoe_nr] -= 1
        revenue_from_shoes += willing_to_pay
        if shoes_dict[desired_shoe_nr] == 0:
            del shoes_dict[desired_shoe_nr]
    return shoes_dict, revenue_from_shoes


def main():
    shoes_quantity = int(input())
    shoes_list = list(map(int, input().split()))
    shoes_dict = Counter(shoes_list)
    customers_number = int(input())
    validate_input(shoes_quantity, customers_number, shoes_list)
    revenue = 0

    for _ in range(customers_number):
        desired_shoe_nr, willing_to_pay = map(int, input().split())
        shoes_dict, revenue = customer_transaction(desired_shoe_nr, shoes_dict, willing_to_pay, revenue)

    print(revenue)


if __name__ == '__main__':
    main()
